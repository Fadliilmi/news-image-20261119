#!/usr/bin/env python3
"""Entry program for news-image-20261119.

Copies the front-page image this repository holds (entry.png, drawn by
draw_news.py from the researched news of Thursday 19 November 2026) to
/output/entry.png. Standard library only, no network, deterministic:
the same bytes every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
print("entry.png written to", OUT_DIR)
sys.exit(0)
