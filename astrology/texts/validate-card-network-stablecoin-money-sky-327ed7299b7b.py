#!/usr/bin/env python3
"""Static integrity checks for the stablecoin product-line Money × Sky surface."""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
SHARED = HERE.parent / "astrology-workbench"
CARDS = HERE / "card_network_stablecoin_astrology_cards.json"
ASTRO = HERE / "CARD_NETWORK_STABLECOIN_ASTROLOGY_DATA_2026-07-29.json"
OUTPUT = HERE / "outputs" / "Card Networks Add Stablecoin Product Lines — Money × Sky.html"
MANIFEST = HERE / "outputs" / "build_manifest.json"

EXPECTED_IDS = [
    "apple_pay_control",
    "visa_acquirer_usdc",
    "visa_bridge_launch",
    "fiserv_fiusd",
    "visa_us_settlement",
    "visa_bridge_expansion",
    "square_bitcoin_terms",
    "mastercard_bvnk",
    "stripe_sessions",
    "paypal_crypto_terms",
    "mastercard_settlement",
    "hyperwallet_pyusd",
    "jcb_circle_mou",
    "visa_vsp",
]


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.articles = 0
        self.details = 0
        self.chart_buttons = 0
        self.source_links = 0
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        classes = set(data.get("class", "").split())
        if tag == "article" and "entry" in classes:
            self.articles += 1
        if tag == "details" and "dd" in classes:
            self.details += 1
        if tag == "button" and "cbtn" in classes:
            self.chart_buttons += 1
        if tag == "a" and data.get("href", "").startswith("http"):
            self.source_links += 1
        if "id" in data:
            if data["id"] in self.ids:
                fail(f"duplicate HTML id: {data['id']}")
            self.ids.add(data["id"])


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    cards = json.loads(CARDS.read_text(encoding="utf-8"))
    astro = json.loads(ASTRO.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    output = OUTPUT.read_text(encoding="utf-8")

    card_ids = [card["id"] for card in cards["cards"]]
    event_ids = [event["id"] for event in astro["events"]]
    if card_ids != EXPECTED_IDS or event_ids != EXPECTED_IDS:
        fail("card/event ids or ordering diverge from the frozen 14-anchor ledger")
    if len(set(event_ids)) != 14:
        fail("event ids are not unique")

    modes = Counter(event["clock_mode"] for event in astro["events"])
    if modes != Counter({"reported": 1, "noon_proxy": 1, "midnight_proxy": 12}):
        fail(f"clock classes changed: {dict(modes)}")
    if astro.get("clock_counts") != {
        "reported": 1,
        "noon_proxy": 1,
        "midnight_proxy": 12,
    }:
        fail("dataset clock-count control is stale")

    for event in astro["events"]:
        context = event.get("contextual_container_clock")
        if not context:
            fail(f"{event['id']} lacks its inspectable chart record")
        dc_context = event.get("dc_companion_clock")
        if not dc_context:
            fail(f"{event['id']} lacks its same-instant D.C. companion")
        if context["utc"] != dc_context["utc"]:
            fail(f"{event['id']} D.C. companion changed the instant")
        for point in ("True Node", "SNode", "Chiron"):
            if point not in context["positions"] or point not in dc_context["positions"]:
                fail(f"{event['id']} lacks required point {point}")
        assumed = event["clock_mode"] != "reported"
        if event.get("angles_assumed") is not assumed:
            fail(f"{event['id']} angle-assumption flag is wrong")
        if event.get("houses_assumed") is not assumed:
            fail(f"{event['id']} house-assumption flag is wrong")
        caption = context.get("caption", "")
        if assumed and "Synthetic" not in caption:
            fail(f"{event['id']} does not label the convention chart synthetic")
        if not assumed and "Reported" not in caption:
            fail("Apple Pay does not retain its reported-clock caption")
        if assumed and "remain convention-derived" not in dc_context.get("caption", ""):
            fail(f"{event['id']} D.C. companion hides its synthetic-angle boundary")
    stripe = next(event for event in astro["events"] if event["id"] == "stripe_sessions")
    if stripe["local_time"] != "12:00" or stripe["clock_mode"] != "noon_proxy":
        fail("Stripe must remain the sole noon-convention chart")
    apple = next(event for event in astro["events"] if event["id"] == "apple_pay_control")
    if apple["local_time"] != "10:47" or apple["clock_mode"] != "reported":
        fail("Apple Pay reported control clock changed")
    america_available = [
        event["id"] for event in astro["events"] if "America" in event["positions"]
    ]
    america_unavailable = [
        event["id"] for event in astro["events"] if "America" not in event["positions"]
    ]
    if america_unavailable != ["apple_pay_control", "visa_acquirer_usdc"]:
        fail(f"unexpected America cache boundary: {america_unavailable}")
    if len(america_available) != 12:
        fail("916 America should be present on the twelve 2025–2026 anchors")
    if astro.get("america_counts") != {"available": 12, "unavailable": 2}:
        fail("America count control is stale")
    if astro.get("dc_companion_count") != 14:
        fail("D.C. companion count control is stale")

    parser = AuditParser()
    parser.feed(output)
    if parser.articles != 14 or parser.details != 14 or parser.chart_buttons != 28:
        fail(
            "HTML counts changed: "
            f"articles={parser.articles}, details={parser.details}, charts={parser.chart_buttons}"
        )
    if parser.source_links < 14:
        fail("one or more cards lacks a source link")
    for required in (
        "1 reported-time chart, 1 noon-convention chart and 12 midnight-convention charts",
        "14 local charts plus 14 Washington, D.C. same-instant companions",
        "916 America: 12 cache-supported anchors",
        "synthetic research geometry",
        "daily backtest was null",
        "No astrological strength or similarity score is computed",
        "Adjacent March and July 2026 releases are temporal clusters",
    ):
        if required not in output and required not in json.dumps(manifest, ensure_ascii=False):
            fail(f"missing method boundary: {required}")
    if "☉" in output or "♄" in output or "♇" in output:
        fail("font astrology glyphs found; canonical wheel requires path glyphs")

    if manifest["cards"] != 14 or manifest["chartable_cards"] != 14:
        fail("manifest counts are stale")
    if manifest.get("wheel_records") != 28:
        fail("manifest D.C.-companion wheel count is stale")
    if manifest["chronology_only_cards"] != 0:
        fail("all 14 anchors should be chartable under the user's convention")
    expected_hashes = {
        CARDS.name: sha256(CARDS),
        ASTRO.name: sha256(ASTRO),
        "vendor/wheel_lib.py": sha256(SHARED / "vendor" / "wheel_lib.py"),
        "vendor/us_rec.json": sha256(SHARED / "vendor" / "us_rec.json"),
    }
    if manifest["source_hashes"] != expected_hashes:
        fail("manifest source hashes are stale")

    print(
        "PASS:",
        "14 cards;",
        "28 wheels;",
        f"{parser.source_links} source links;",
        "clock ledger 1 reported / 1 noon / 12 midnight;",
        "synthetic-angle boundary intact",
    )


if __name__ == "__main__":
    main()
