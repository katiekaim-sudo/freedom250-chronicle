#!/usr/bin/env python3
"""Static integrity checks for the credit-card transition card plot."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
CARDS = HERE / "credit_card_transition_cards.json"
ASTRO = HERE.parent / "CREDIT_CARD_TRANSITION_ASTROLOGY_DATA_2026-07-28.json"
OUTPUT = HERE / "outputs" / "Credit Card Transition — Money × Sky.html"
MANIFEST = HERE / "outputs" / "build_manifest.json"


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
                raise ValueError(f"duplicate HTML id: {data['id']}")
            self.ids.add(data["id"])


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    cards = json.loads(CARDS.read_text(encoding="utf-8"))
    astro = json.loads(ASTRO.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    output = OUTPUT.read_text(encoding="utf-8")

    card_ids = [card["id"] for card in cards["cards"]]
    event_ids = [event["id"] for event in astro["events"]]
    if len(card_ids) != len(set(card_ids)):
        fail("card ids are not unique")
    if set(card_ids) != set(event_ids):
        fail(f"card/event id mismatch: cards={set(card_ids)} events={set(event_ids)}")
    if card_ids != event_ids:
        fail("card and event ordering diverges")

    point_events = [event for event in astro["events"] if event.get("positions")]
    context_events = [
        event for event in astro["events"] if event.get("contextual_container_clock")
    ]
    if [event["id"] for event in context_events] != ["apple_pay"]:
        fail("only Apple Pay may carry a context clock")
    for event in point_events:
        if event["id"] != "apple_pay":
            if not event.get("angles_withheld") or not event.get("houses_withheld"):
                fail(f"{event['id']} silently acquired event angles or houses")
    securitization = next(event for event in astro["events"] if event["id"] == "securitization")
    if securitization.get("point_chart") is not None or securitization.get("positions"):
        fail("securitization must remain chronology-only")

    parser = AuditParser()
    parser.feed(output)
    expected_cards = len(cards["cards"])
    expected_charts = len(point_events)
    if parser.articles != expected_cards:
        fail(f"expected {expected_cards} cards, found {parser.articles}")
    if parser.details != expected_cards:
        fail(f"expected {expected_cards} detail drawers, found {parser.details}")
    if parser.chart_buttons != expected_charts:
        fail(f"expected {expected_charts} chart buttons, found {parser.chart_buttons}")
    if parser.source_links < expected_cards:
        fail("one or more cards lacks a source link")
    for required in (
        "open buildup + reading",
        "Exact geometry shown",
        "Counterweight / provenance",
        "The adapter story gets stronger if",
        "The adapter story weakens if",
        "The project’s own daily backtest was null",
        "No astrological strength or similarity score is computed",
    ):
        if required not in output and required not in json.dumps(manifest, ensure_ascii=False):
            fail(f"missing required method text: {required}")
    if "☉" in output or "♄" in output or "♇" in output:
        fail("font astrology glyphs found; canonical wheel requires path glyphs")
    if manifest["cards"] != expected_cards:
        fail("manifest card count is stale")

    print(
        "PASS:",
        f"{parser.articles} cards;",
        f"{parser.chart_buttons} chart buttons;",
        f"{parser.source_links} source links;",
        "clock boundaries intact",
    )


if __name__ == "__main__":
    main()
