#!/usr/bin/env python3
"""Build the stablecoin product-line Money × Sky card surface."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SHARED = HERE.parent.parent / "astrology-workbench"
SHARED_BUILDER = SHARED / "build_credit_card_transition_cards.py"

spec = importlib.util.spec_from_file_location("shared_money_sky_builder", SHARED_BUILDER)
builder = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(builder)

builder.CARDS_PATH = HERE / "card_network_stablecoin_astrology_cards.json"
builder.ASTRO_PATH = HERE / "CARD_NETWORK_STABLECOIN_ASTROLOGY_DATA_2026-07-29.json"
builder.US_PATH = SHARED / "vendor" / "us_rec.json"
builder.WHEEL_PATH = SHARED / "vendor" / "wheel_lib.py"
builder.OUT_PATH = HERE / "outputs" / "Card Networks Add Stablecoin Product Lines — Money × Sky.html"
builder.MANIFEST_PATH = HERE / "outputs" / "build_manifest.json"


if __name__ == "__main__":
    builder.main()
