#!/usr/bin/env python3
"""Build the Chronicle-owned Astrology Files data and room.

Astrology Files is an independent Sky & Charts collection.  It does not read
the Freedom 250 Research Workbench, Research Registry, or Research Desk data.
The catalog owns collection-level presentation; the registry owns exact file
membership.  Every source path must resolve beneath ``03 - Astrology/Astrology
Files`` so the projection cannot silently reach into government Research.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import html
import io
import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote

from atomic_io import atomic_write_text


HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
ASTROLOGY_ROOT = VAULT / "03 - Astrology" / "Astrology Files"
CATALOG = ASTROLOGY_ROOT / "ASTROLOGY FILES CATALOG.json"
REGISTRY = ASTROLOGY_ROOT / "ASTROLOGY FILES REGISTRY.json"
DATA_OUT = VAULT / "99 - Templates" / "astrology_files_data.json"
HTML_OUT = VAULT / "04 - Synthesis" / "Cross-cuts" / "Astrology Reference Room.html"
VISUAL_OUT = VAULT / "04 - Synthesis" / "Cross-cuts" / "Astrology Files Assets"

ASTROLOGY_ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
READABLE_SUFFIXES = {".md", ".txt", ".json", ".csv", ".tsv", ".py", ".js", ".css"}
PACKAGE_STATES = {"current", "archive"}
FILE_STATES = {"current", "draft", "archive"}
MAX_TEXT_BYTES = 1_500_000


def die(message: str) -> None:
    raise SystemExit(f"Astrology Files build FAILED: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        die(f"cannot read {path}: {exc}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_text(owner: str, value: dict, field: str) -> str:
    result = value.get(field)
    if not isinstance(result, str) or not result.strip():
        die(f"{owner} requires nonblank {field}")
    return result.strip()


def safe_source(relative: str, *, owner: str) -> Path:
    """Resolve one catalog/registry path and prove Astrology Files ownership."""
    if not isinstance(relative, str) or not relative.strip():
        die(f"{owner} has a blank path")
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        die(f"{owner} has unsafe path {relative!r}")
    required_prefix = Path("03 - Astrology") / "Astrology Files"
    try:
        candidate.relative_to(required_prefix)
    except ValueError:
        die(
            f"{owner} must use a vault-relative path beneath "
            f"03 - Astrology/Astrology Files: {relative!r}"
        )
    root = ASTROLOGY_ROOT.resolve()
    target = (VAULT / candidate).resolve()
    try:
        target.relative_to(root)
    except ValueError:
        die(f"{owner} escapes Astrology Files: {relative!r}")
    if not target.exists():
        die(f"{owner} points to missing Astrology Files path {relative!r}")
    return target


def safe_asset_name(value: str, source: Path, *, owner: str) -> str:
    name = value.strip() if isinstance(value, str) else ""
    name = name or source.name
    if Path(name).name != name or name in {".", ".."}:
        die(f"{owner} has unsafe asset_name {name!r}")
    return name


def safe_markdown(text: str) -> str:
    """Small, deliberately non-executable Markdown reader."""
    # Obsidian metadata governs the document but is not part of its reading
    # surface. Strip only a real opening YAML fence; later horizontal rules stay.
    if text.startswith("\ufeff"):
        text = text.lstrip("\ufeff")
    if text.startswith("---\n") or text.startswith("---\r\n"):
        frontmatter_end = re.search(r"\r?\n---\r?\n", text[3:])
        if frontmatter_end:
            text = text[3 + frontmatter_end.end():]
    lines = text.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    quote: list[str] = []
    in_list = False
    in_code = False

    def inline(value: str) -> str:
        value = html.escape(value, quote=True)
        value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
        value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
        return value

    def flush() -> None:
        nonlocal paragraph
        if paragraph:
            output.append("<p>" + inline(" ".join(x.strip() for x in paragraph)) + "</p>")
            paragraph = []

    def flush_quote() -> None:
        nonlocal quote
        if quote:
            output.append("<blockquote><p>" + inline(" ".join(quote)) + "</p></blockquote>")
            quote = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            flush_quote()
            if in_list:
                output.append("</ul>")
                in_list = False
            output.append("</code></pre>" if in_code else "<pre><code>")
            in_code = not in_code
            continue
        if in_code:
            output.append(html.escape(line) + "\n")
            continue
        if stripped.startswith(">"):
            flush()
            if in_list:
                output.append("</ul>")
                in_list = False
            quote.append(stripped[1:].lstrip())
            continue
        flush_quote()
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        if heading:
            flush()
            if in_list:
                output.append("</ul>")
                in_list = False
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif bullet:
            flush()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append("<li>" + inline(bullet.group(1)) + "</li>")
        elif not stripped:
            flush()
            if in_list:
                output.append("</ul>")
                in_list = False
        else:
            if in_list:
                output.append("</ul>")
                in_list = False
            paragraph.append(line)
    flush()
    flush_quote()
    if in_list:
        output.append("</ul>")
    if in_code:
        output.append("</code></pre>")
    return "".join(output)


def render_delimited(text: str, delimiter: str) -> str:
    rows = list(csv.reader(io.StringIO(text), delimiter=delimiter))
    if not rows:
        return "<p>This file is empty.</p>"
    clipped = rows[:1000]
    width = max(len(row) for row in clipped)
    body: list[str] = ["<div class=table-wrap><table>"]
    for row_no, row in enumerate(clipped):
        tag = "th" if row_no == 0 else "td"
        body.append("<tr>" + "".join(f"<{tag}>{html.escape(cell)}</{tag}>" for cell in row + [""] * (width - len(row))) + "</tr>")
    body.append("</table></div>")
    if len(rows) > len(clipped):
        body.append(f"<p>Showing the first {len(clipped):,} rows.</p>")
    return "".join(body)


def render_document(path: Path) -> tuple[str, bool]:
    if path.is_dir() or path.suffix.lower() not in READABLE_SUFFIXES:
        return "", False
    raw = path.read_bytes()
    truncated = len(raw) > MAX_TEXT_BYTES
    text = raw[:MAX_TEXT_BYTES].decode("utf-8", errors="replace")
    suffix = path.suffix.lower()
    if suffix == ".md":
        rendered = safe_markdown(text)
    elif suffix == ".json":
        try:
            text = json.dumps(json.loads(text), ensure_ascii=False, indent=2)
        except json.JSONDecodeError:
            pass
        rendered = "<pre><code>" + html.escape(text) + "</code></pre>"
    elif suffix in {".csv", ".tsv"}:
        rendered = render_delimited(text, "," if suffix == ".csv" else "\t")
    else:
        rendered = "<pre><code>" + html.escape(text) + "</code></pre>"
    if truncated:
        rendered += "<p><em>Preview truncated; the full file remains at the listed path.</em></p>"
    return rendered, truncated


def normalize_ids(value, *, owner: str) -> list[str]:
    if not isinstance(value, list) or not value:
        die(f"{owner} requires a nonempty astrology_ids list")
    if any(not isinstance(item, str) or not ASTROLOGY_ID_RE.fullmatch(item) for item in value):
        die(f"{owner} has a malformed astrology_id")
    if len(value) != len(set(value)):
        die(f"{owner} has duplicate astrology_ids")
    return value


def validate_catalog(document: object) -> tuple[dict, list[dict]]:
    if not isinstance(document, dict) or document.get("schema") != "f250.astrology-files-catalog/v1":
        die("Catalog schema must be f250.astrology-files-catalog/v1")
    packages = document.get("packages")
    if not isinstance(packages, list) or not packages:
        die("Catalog packages must be a nonempty list")
    seen: set[str] = set()
    normalized: list[dict] = []
    for package in packages:
        if not isinstance(package, dict):
            die("Catalog contains a non-object package")
        astrology_id = require_text("Catalog package", package, "astrology_id")
        if not ASTROLOGY_ID_RE.fullmatch(astrology_id) or astrology_id in seen:
            die(f"Catalog has malformed or duplicate astrology_id {astrology_id!r}")
        if "research_id" in package:
            die(f"{astrology_id} uses retired research_id; use astrology_id")
        seen.add(astrology_id)
        for field in ("title", "lane", "summary", "developed_through"):
            require_text(astrology_id, package, field)
        if package.get("shelf") not in PACKAGE_STATES:
            die(f"{astrology_id} has invalid shelf")
        item = dict(package)
        item["library_state"] = item["shelf"]
        normalized.append(item)
    declared = document.get("astrology_ids")
    if declared is not None and set(normalize_ids(declared, owner="Catalog")) != seen:
        die("Catalog astrology_ids must exactly match package astrology_id values")
    return document, normalized


def validate_registry(document: object, known_ids: set[str]) -> tuple[dict, list[dict]]:
    if not isinstance(document, dict) or document.get("schema") != "f250.astrology-files-registry/v1":
        die("Registry schema must be f250.astrology-files-registry/v1")
    rows = document.get("artifacts")
    if not isinstance(rows, list) or not rows:
        die("Registry artifacts must be a nonempty list")
    seen: set[str] = set()
    normalized: list[dict] = []
    for row in rows:
        if not isinstance(row, dict):
            die("Registry contains a non-object artifact")
        path = require_text("Registry artifact", row, "path")
        if path in seen:
            die(f"Registry has duplicate path {path!r}")
        seen.add(path)
        ids = normalize_ids(row.get("astrology_ids"), owner=f"Registry {path}")
        dangling = sorted(set(ids) - known_ids)
        if dangling:
            die(f"Registry {path} has unknown astrology_ids {dangling}")
        state = row.get("file_state", row.get("state", "current"))
        if state not in FILE_STATES:
            die(f"Registry {path} has invalid file_state {state!r}")
        source = safe_source(path, owner=f"Registry {path}")
        item = dict(row)
        expected_bytes = row.get("bytes")
        expected_hash = row.get("sha256")
        actual_bytes = source.stat().st_size if source.is_file() else 0
        actual_hash = sha256(source) if source.is_file() else ""
        if expected_bytes is not None and expected_bytes != actual_bytes:
            die(f"Registry {path} bytes mismatch: expected {expected_bytes}, found {actual_bytes}")
        if expected_hash not in (None, "") and expected_hash != actual_hash:
            die(f"Registry {path} sha256 mismatch")
        controlling = row.get("controlling_path")
        if controlling not in (None, "", path):
            safe_source(controlling, owner=f"Registry {path} controlling_path")
        item.update({
            "artifact_id": "astro-" + hashlib.sha256(path.encode()).hexdigest()[:16],
            "path": path,
            "absolute_path": str(source),
            "astrology_ids": ids,
            "file_state": state,
            "display_title": row.get("title") or source.name,
            "artifact_role": row.get("artifact_role", row.get("role", "other")),
            "description": row.get("description", ""),
            "size_bytes": actual_bytes,
            "bytes": actual_bytes,
            "sha256": actual_hash,
        })
        item["content_html"], item["content_truncated"] = render_document(source)
        item["readable"] = bool(item["content_html"])
        normalized.append(item)
    aliases = {}
    for row in normalized:
        for alias in (row["path"], row.get("legacy_workbench_path")):
            if not alias:
                continue
            candidate = Path(alias)
            if candidate.is_absolute() or ".." in candidate.parts:
                die(f"Registry has unsafe legacy path {alias!r}")
            if alias in aliases and aliases[alias] != row["path"]:
                die(f"Registry has ambiguous Astrology document alias {alias!r}")
            aliases[alias] = row["path"]
    for astrology_id in known_ids:
        if not any(astrology_id in row["astrology_ids"] for row in normalized):
            die(f"{astrology_id} has no Registry artifacts")
    return document, normalized


def document_ref(value: object, *, owner: str, registry_by_path: dict[str, dict]) -> dict:
    if not isinstance(value, dict):
        die(f"{owner} must be an object")
    if value.get("scope", "vault") != "vault":
        die(f"{owner} scope must be vault")
    path = require_text(owner, value, "path")
    if path not in registry_by_path:
        die(f"{owner} path is not in Astrology Files Registry: {path!r}")
    item = dict(registry_by_path[path])
    if value.get("role"):
        item["role"] = value["role"]
    return item


def stage_visual(value: object, *, owner: str, registry_by_path: dict[str, dict], seen_assets: set[str]) -> dict:
    if not isinstance(value, dict):
        die(f"{owner} visual must be an object")
    if value.get("scope", "vault") != "vault":
        die(f"{owner} visual scope must be vault")
    path = require_text(f"{owner} visual", value, "path")
    if path not in registry_by_path:
        die(f"{owner} visual is not in Astrology Files Registry: {path!r}")
    source = safe_source(path, owner=f"{owner} visual")
    asset_name = safe_asset_name(value.get("asset_name", ""), source, owner=owner)
    if asset_name in seen_assets:
        die(f"duplicate Astrology Files visual asset_name {asset_name!r}")
    seen_assets.add(asset_name)
    destination = VISUAL_OUT / asset_name
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination, dirs_exist_ok=True)
        launch = destination / "index.html"
        if not launch.is_file():
            die(f"{owner} visual directory has no index.html")
    else:
        shutil.copy2(source, destination)
        launch = destination
    result = dict(value)
    result.update({
        "path": path,
        "absolute_path": str(source),
        "asset_name": asset_name,
        "local_path": quote("Astrology Files Assets/" + asset_name) + ("/index.html" if source.is_dir() else ""),
    })
    return result


def build_snapshot() -> dict:
    catalog_doc, packages = validate_catalog(load_json(CATALOG))
    known_ids = {package["astrology_id"] for package in packages}
    registry_doc, artifacts = validate_registry(load_json(REGISTRY), known_ids)
    registry_by_path = {row["path"]: row for row in artifacts}
    refs_by_id = {
        astrology_id: [row for row in artifacts if astrology_id in row["astrology_ids"]]
        for astrology_id in known_ids
    }
    seen_assets: set[str] = set()
    enriched: list[dict] = []
    for package in packages:
        astrology_id = package["astrology_id"]
        p = dict(package)
        read_first = document_ref(p.get("read_first"), owner=f"{astrology_id} read_first", registry_by_path=registry_by_path)
        supporting = [
            document_ref(item, owner=f"{astrology_id} supporting", registry_by_path=registry_by_path)
            for item in p.get("supporting", [])
        ]
        selected = {read_first["path"], *(item["path"] for item in supporting)}
        remaining = [dict(item) for item in refs_by_id[astrology_id] if item["path"] not in selected]
        artifact_refs = p.get("artifact_refs")
        if not isinstance(artifact_refs, list) or len(artifact_refs) != len(set(artifact_refs)):
            die(f"{astrology_id} artifact_refs must be a unique list")
        registry_paths = {item["path"] for item in refs_by_id[astrology_id]}
        if set(artifact_refs) != registry_paths:
            missing = sorted(registry_paths - set(artifact_refs))
            extra = sorted(set(artifact_refs) - registry_paths)
            die(f"{astrology_id} artifact_refs do not match Registry (missing={missing}, extra={extra})")
        p["read_first"] = read_first
        p["supporting"] = supporting
        p["documents"] = [read_first, *supporting, *remaining]
        p["registry_refs"] = [item["path"] for item in refs_by_id[astrology_id]]
        p["visuals"] = [
            stage_visual(item, owner=astrology_id, registry_by_path=registry_by_path, seen_assets=seen_assets)
            for item in p.get("visuals", [])
        ]
        enriched.append(p)
    by_id = {package["astrology_id"]: package for package in enriched}
    for package in enriched:
        relations = package.get("relations", {})
        if relations is None:
            relations = {}
        if not isinstance(relations, dict):
            die(f"{package['astrology_id']} relations must be an object")
        targets = [relations.get("parent_id"), relations.get("rolled_into_id")]
        for key in ("supersedes_ids", "related_ids"):
            values = relations.get(key, [])
            if not isinstance(values, list):
                die(f"{package['astrology_id']} {key} must be a list")
            targets.extend(values)
        dangling = [target for target in targets if target and target not in by_id]
        if dangling:
            die(f"{package['astrology_id']} has dangling relationships {dangling}")
        package["relationship_links"] = [
            {"astrology_id": target, "title": by_id[target]["title"]}
            for target in dict.fromkeys(target for target in targets if target)
        ]
    generated_at = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    return {
        "schema_version": "f250.astrology-files-data/v1",
        "generated_at": generated_at,
        "purpose": catalog_doc.get("purpose", ""),
        "workflow_boundary": catalog_doc.get("workflow_boundary", {}),
        "method_boundary": "Mundane facts are followed first. Astrology is analyzed separately. Natural overlaps are compared afterward; astrology never creates, upgrades, corroborates, or substitutes for factual evidence.",
        "authority": str(ASTROLOGY_ROOT),
        "source_hashes": {
            "catalog_sha256": sha256(CATALOG),
            "registry_sha256": sha256(REGISTRY),
        },
        "packages": enriched,
        "artifacts": artifacts,
        "lanes": list(dict.fromkeys(package["lane"] for package in enriched)),
        "stats": {
            "saved_astrology": len(enriched),
            "current": sum(package["library_state"] == "current" for package in enriched),
            "archive": sum(package["library_state"] == "archive" for package in enriched),
            "artifacts": len(artifacts),
            "readable_artifacts": sum(item["readable"] for item in artifacts),
            "visuals": sum(len(package.get("visuals", [])) for package in enriched),
        },
    }


def build_html(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Astrology Files — Freedom 250 Observatory</title>
<style>:root{--paper:#f3efe7;--panel:#fffdf8;--ink:#24211d;--muted:#716a60;--line:#d9d0c1;--violet:#7552a3;--shadow:0 12px 34px rgba(45,35,27,.17)}*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:var(--paper);color:var(--ink);font:15px/1.5 Arial,sans-serif}button,input{font:inherit;color:inherit}.top{position:sticky;top:0;z-index:20;background:rgba(243,239,231,.96);border-bottom:1px solid var(--line);padding:18px 22px}.mast{max-width:1250px;margin:auto;display:flex;justify-content:space-between;gap:18px;align-items:end}.eyebrow{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--violet);font-weight:800}.title{font:700 30px/1.1 Georgia,serif}.sub,.stats{font-size:12px;color:var(--muted)}.wrap{max-width:1250px;margin:auto;padding:22px 22px 70px}.intro{max-width:820px;margin:0 0 16px;color:var(--muted)}.boundary{border-left:4px solid var(--violet);background:#f4eef9;padding:10px 13px;margin:0 0 17px;max-width:900px}.toolbar{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:18px}.search{flex:1;min-width:260px;border:1px solid var(--line);background:var(--panel);padding:10px 12px;border-radius:8px}.chip{border:1px solid var(--line);background:var(--panel);border-radius:999px;padding:7px 11px;cursor:pointer;font-size:12px}.chip.active{border-color:var(--violet);box-shadow:inset 0 0 0 1px var(--violet)}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:12px}.card{min-height:205px;text-align:left;border:1px solid var(--line);background:var(--panel);border-radius:10px;padding:15px;cursor:pointer;display:flex;flex-direction:column}.card:hover{border-color:var(--violet);box-shadow:var(--shadow);transform:translateY(-1px)}.lane{font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--violet);font-weight:800}.card h2{font:700 19px/1.25 Georgia,serif;margin:7px 0}.bluf{font-size:13px;color:#4c463f;flex:1}.cutoff{font-size:11px;color:var(--muted);margin-top:10px}.archive{display:inline-block;border:1px solid #c8b4df;color:var(--violet);border-radius:4px;padding:2px 6px;font-size:9px;text-transform:uppercase}.empty{border:1px dashed var(--line);padding:28px;text-align:center;color:var(--muted);border-radius:9px}.overlay{position:fixed;inset:0;background:rgba(23,19,28,.52);z-index:80;display:none}.overlay.open{display:block}.drawer{position:absolute;right:0;top:0;width:min(830px,97vw);height:100%;overflow:auto;background:var(--panel);padding:25px 28px 70px;box-shadow:-12px 0 42px rgba(0,0,0,.24)}.close{position:sticky;top:0;float:right;border:1px solid var(--line);background:var(--panel);border-radius:999px;width:36px;height:36px;cursor:pointer}.drawer h2{font:700 28px/1.15 Georgia,serif;margin:6px 44px 10px 0}.lead{font:17px/1.55 Georgia,serif}.rule{border-left:4px solid var(--violet);background:#f4eef9;padding:11px 13px;margin:16px 0}.rule b{display:block;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--violet);margin-bottom:4px}.facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin:14px 0}.fact{border:1px solid var(--line);border-radius:6px;padding:9px;font-size:12px}.fact b{display:block;font-size:9px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}.drawer h3{font:700 17px Georgia,serif;margin:22px 0 8px}.links,.relations{display:flex;gap:6px;flex-wrap:wrap}.small{border:1px solid var(--line);background:var(--paper);border-radius:5px;padding:5px 8px;font-size:10px;cursor:pointer;color:var(--violet)}.docs{display:grid;gap:7px}.doc{border:1px solid var(--line);border-radius:7px;padding:10px;cursor:pointer}.doc.selected{border-color:var(--violet);box-shadow:inset 4px 0 0 var(--violet)}.doc b{display:block}.path{font:9px/1.4 ui-monospace,monospace;color:var(--muted);word-break:break-all}.reader{border-top:1px solid var(--line);margin-top:18px;padding-top:16px}.reader-body{font:14px/1.65 Georgia,serif}.reader-body pre{white-space:pre-wrap;overflow:auto;background:#eee8dc;padding:10px}.table-wrap{overflow:auto}.reader-body table{border-collapse:collapse;font:11px/1.35 ui-monospace,monospace}.reader-body th,.reader-body td{border:1px solid var(--line);padding:4px 6px;vertical-align:top}.visual{width:100%;text-align:left;border:1px solid var(--line);background:var(--paper);border-radius:7px;padding:10px;cursor:pointer}.visual-frame{position:fixed;inset:12px;width:calc(100% - 24px);height:calc(100% - 24px);border:0;background:#fff;z-index:120;display:none;border-radius:8px}.visual-frame.open{display:block}.visual-close{position:fixed;right:24px;top:24px;z-index:121;display:none}.visual-close.open{display:block}html[data-theme="dark"]{--paper:#17141b;--panel:#211d26;--ink:#eee8f4;--muted:#afa5b5;--line:#48404f;--violet:#c6a3ef}html[data-theme="dark"] .rule,html[data-theme="dark"] .boundary{background:#2b2333}html[data-theme="dark"] .reader-body pre{background:#17141b}@media(max-width:650px){.mast{display:block}.stats{margin-top:8px}.facts{grid-template-columns:1fr}.drawer{padding:18px 17px 55px}.wrap{padding:18px 13px 55px}}</style></head><body>
<header class="top"><div class="mast"><div><div class="eyebrow">Sky &amp; Charts</div><div class="title">Astrology Files</div><div class="sub" id="stamp"></div></div><div class="stats" id="stats"></div></div></header><main class="wrap"><p class="intro">Methods, chart experiments, persona work and interpretive overlays live here as their own Observatory collection—not in government Research.</p><div class="boundary" id="boundary"></div><div class="toolbar"><input id="search" class="search" type="search" placeholder="Search astrology files, methods, charts and personas…" aria-label="Search Astrology Files"><button class="chip active" data-lane="all">All</button><span id="lanes"></span></div><div class="grid" id="grid"></div></main>
<div class="overlay" id="overlay" role="dialog" aria-modal="true" aria-labelledby="drawerTitle"><aside class="drawer"><button class="close" id="close" aria-label="Close Astrology File">×</button><div id="drawer"></div></aside></div><button class="small visual-close" id="visualClose">Close visual</button><iframe class="visual-frame" id="visualFrame" title="Astrology visual"></iframe><script id="astrology-data" type="application/json">__DATA__</script>
<script>(function(){'use strict';var D=JSON.parse(document.getElementById('astrology-data').textContent),items=D.packages||[],byId={},docByPath={},docByArtifact={},lane='all',query='',docs=[];items.forEach(function(p){byId[p.astrology_id]=p;(p.documents||[]).forEach(function(d){[d.path,d.legacy_workbench_path].filter(Boolean).forEach(function(path){var hit=docByPath[path];if(hit&&hit.doc.path!==d.path)throw new Error('Ambiguous Astrology document alias: '+path);docByPath[path]={package:p,doc:d};});docByArtifact[d.artifact_id]={package:p,doc:d};});});function esc(s){var d=document.createElement('div');d.textContent=s==null?'':String(s);return d.innerHTML;}function card(p){return '<button class="card" data-open="'+esc(p.astrology_id)+'"><div class="lane">'+esc(p.lane)+'</div><h2>'+esc(p.title)+'</h2><p class="bluf">'+esc(p.summary)+'</p>'+(p.library_state==='archive'?'<div><span class="archive">Archive</span></div>':'')+'<div class="cutoff">Developed through '+esc(p.developed_through)+' · '+(p.documents||[]).length+' files</div></button>';}function render(){var q=query.toLowerCase(),rows=items.filter(function(p){return(lane==='all'||p.lane===lane)&&(!q||[p.title,p.summary,p.question,p.purpose,(p.entities||[]).join(' '),(p.search_terms||[]).join(' '),(p.registry_refs||[]).join(' ')].join(' ').toLowerCase().indexOf(q)>=0);});document.getElementById('grid').innerHTML=rows.length?rows.map(card).join(''):'<div class="empty">No Astrology Files match this search.</div>';}function docRow(d,i){return '<div class="doc" tabindex="0" data-doc="'+i+'"><b>'+esc(d.role||d.artifact_role||(i?'Saved file':'Start here'))+'</b><div>'+esc(d.display_title||d.path.split('/').pop())+'</div><div class="path">'+esc(d.path)+'</div></div>';}function showDoc(i){var d=docs[i];if(!d)return;document.querySelectorAll('[data-doc]').forEach(function(x){x.classList.toggle('selected',Number(x.dataset.doc)===i);});document.getElementById('readerTitle').textContent=d.display_title||d.path.split('/').pop();document.getElementById('readerBody').innerHTML=d.content_html||'<p>This file is preserved at:</p><div class="path">'+esc(d.absolute_path)+'</div>';}function openItem(id,path,artifactId){var p=byId[id];if(!p)return;docs=p.documents||[];var intent=p.question||p.purpose||'',relations=(p.relationship_links||[]).map(function(r){return '<button class="small" data-open="'+esc(r.astrology_id)+'">'+esc(r.title)+'</button>';}).join(''),views=(p.view_links||[]).map(function(v){return '<button class="small" data-tab="'+esc(v.tab)+'">↗ '+esc(v.label)+'</button>';}).join(''),visuals=(p.visuals||[]).map(function(v){return '<button class="visual" data-visual="'+esc(v.local_path)+'">'+esc(v.title||v.asset_name)+'</button>';}).join('');document.getElementById('drawer').innerHTML='<div class="lane">'+esc(p.lane)+'</div><h2 id="drawerTitle">'+esc(p.title)+'</h2><p class="lead">'+esc(p.summary)+'</p>'+(intent?'<div class="rule"><b>Purpose / question</b>'+esc(intent)+'</div>':'')+'<div class="facts"><div class="fact"><b>Developed through</b>'+esc(p.developed_through)+'</div><div class="fact"><b>Saved material</b>'+docs.length+' files · '+(p.visuals||[]).length+' visuals</div></div>'+(p.use_note?'<div class="rule"><b>Useful context</b>'+esc(p.use_note)+'</div>':'')+(relations?'<h3>Related Astrology Files</h3><div class="relations">'+relations+'</div>':'')+(views?'<h3>Sky &amp; Charts</h3><div class="links">'+views+'</div>':'')+(visuals?'<h3>Interactive visuals</h3>'+visuals:'')+'<h3>Files</h3><div class="docs">'+docs.map(docRow).join('')+'</div><section class="reader"><h3 id="readerTitle"></h3><div class="reader-body" id="readerBody"></div></section>';document.getElementById('overlay').classList.add('open');document.body.style.overflow='hidden';var index=0,exactDocument=false;if(path)docs.some(function(d,i){if(d.path===path){index=i;exactDocument=true;return true;}return false;});else if(artifactId)docs.some(function(d,i){if(d.artifact_id===artifactId){index=i;exactDocument=true;return true;}return false;});showDoc(index);if(exactDocument)document.getElementById('readerTitle').scrollIntoView({block:'start'});}function openDocument(m){var hit=(m.path&&docByPath[m.path])||(m.artifact_id&&docByArtifact[m.artifact_id]);if(hit)openItem(hit.package.astrology_id,hit.doc.path,hit.doc.artifact_id);}function close(){document.getElementById('overlay').classList.remove('open');document.body.style.overflow='';}document.addEventListener('click',function(e){var b=e.target.closest('button,[data-open],[data-tab],[data-doc],[data-visual]');if(!b)return;if(b.dataset.open)openItem(b.dataset.open);else if(b.dataset.tab)window.parent.postMessage({action:'navigateTo',tab:b.dataset.tab},'*');else if(b.dataset.doc!==undefined)showDoc(Number(b.dataset.doc));else if(b.dataset.visual){document.getElementById('visualFrame').src=b.dataset.visual;document.getElementById('visualFrame').classList.add('open');document.getElementById('visualClose').classList.add('open');}else if(b.id==='visualClose'){document.getElementById('visualFrame').classList.remove('open');document.getElementById('visualFrame').removeAttribute('src');b.classList.remove('open');}else if(b.id==='close')close();else if(b.dataset.lane!==undefined){document.querySelectorAll('[data-lane]').forEach(function(x){x.classList.remove('active');});b.classList.add('active');lane=b.dataset.lane;render();}});document.getElementById('overlay').addEventListener('click',function(e){if(e.target===this)close();});document.getElementById('search').addEventListener('input',function(){query=this.value.trim();render();});window.addEventListener('message',function(e){var m=e.data||{};if(m.action==='setTheme')document.documentElement.setAttribute('data-theme',m.theme||'light');if((m.action==='openAstrology'||m.action==='openResearch')&&m.id)openItem(m.id,m.path,m.artifact_id);if(m.action==='openAstrologyDocument'||m.action==='openResearchDocument')openDocument(m);});document.getElementById('lanes').innerHTML=(D.lanes||[]).map(function(l){return '<button class="chip" data-lane="'+esc(l)+'">'+esc(l)+'</button>';}).join(' ');document.getElementById('boundary').textContent=D.method_boundary||'';document.getElementById('stamp').textContent='Built '+D.generated_at.replace('T',' ')+' · independent Sky & Charts collection';document.getElementById('stats').textContent=D.stats.saved_astrology+' collections · '+D.stats.artifacts+' files · '+D.stats.archive+' archived';render();})();</script></body></html>'''
    return template.replace("__DATA__", payload)


def main() -> None:
    data = build_snapshot()
    atomic_write_text(DATA_OUT, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    atomic_write_text(HTML_OUT, build_html(data))
    print(
        f"Astrology Files: {data['stats']['saved_astrology']} collections, "
        f"{data['stats']['artifacts']} files, {data['stats']['visuals']} visuals"
    )
    print(f"Wrote {DATA_OUT}")
    print(f"Wrote {HTML_OUT}")


if __name__ == "__main__":
    main()
