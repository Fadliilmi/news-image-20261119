#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

Own work: every shape and line of text is drawn here with Pillow from the
researched stories of Thursday 19 November 2026. Run:
    python3 draw_news.py   -> writes entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
NAVY = (20, 33, 61)
GOLD = (176, 141, 60)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
GREY = (90, 90, 90)
RULE = (120, 110, 95)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead -------------------------------------------------------------
d.rectangle([0, 0, W, 108], fill=NAVY)
d.text((32, 10), "THE WORLD IN ONE DAY", font=font(SERIF_B, 56), fill=(255, 255, 255))
d.text((32, 70), "THURSDAY  ·  19 NOVEMBER 2026", font=font(SANS_B, 28), fill=(232, 196, 106))
d.text((716, 74), "ONE DAY  ·  ONE IMAGE", font=font(SANS, 21), fill=(200, 205, 220))

# ---- lead story: ICJ Rohingya ruling --------------------------------------
d.text((32, 128), "THE HAGUE  —  WORLD COURT RULES", font=font(SANS_B, 23), fill=RED)
y = 158
y = para(d, 32, y, "MYANMAR GUILTY", font(SERIF_B, 54), 620, 58)
y = para(d, 32, y, "OF GENOCIDE", font(SERIF_B, 54), 620, 58)
y += 4
y = para(d, 32, y, "The International Court of Justice finds Myanmar guilty of "
        "genocide against the Rohingya — the first such ruling against "
        "a state.",
        font(SERIF, 24), 620, 30)
# scales-of-justice panel
d.rectangle([690, 128, 992, 336], fill=(233, 220, 180), outline=GOLD, width=4)
cx, top = 841, 152
d.line([cx, top, cx, top + 118], fill=INK, width=6)
d.line([cx - 88, top + 22, cx + 88, top + 22], fill=INK, width=6)
d.line([cx - 88, top + 22, cx - 58, top + 78], fill=INK, width=4)
d.line([cx - 88, top + 22, cx - 118, top + 78], fill=INK, width=4)
d.line([cx + 88, top + 22, cx + 58, top + 78], fill=INK, width=4)
d.line([cx + 88, top + 22, cx + 118, top + 78], fill=INK, width=4)
d.arc([cx - 118, top + 62, cx - 58, top + 106], 0, 180, fill=INK, width=4)
d.arc([cx + 58, top + 62, cx + 118, top + 106], 0, 180, fill=INK, width=4)
d.line([cx - 52, top + 118, cx + 52, top + 118], fill=INK, width=6)
d.line([cx - 34, top + 130, cx + 34, top + 130], fill=INK, width=6)
d.text((716, 296), "THE HAGUE  ·  ICJ", font=font(SANS_B, 22), fill=INK)
d.line([32, 384, 992, 384], fill=RULE, width=3)

# ---- second row: summit + markets -----------------------------------------
y = 402
d.text((32, y), "SHENZHEN  —  SUMMIT", font=font(SANS_B, 21), fill=TEAL)
y2 = para(d, 32, y + 28, "TRUMP, XI AND PUTIN", font(SERIF_B, 33), 460, 39)
y2 = para(d, 32, y2, "MEET FACE TO FACE", font(SERIF_B, 33), 460, 39)
y2 = para(d, 32, y2 + 4, "First three-way summit of the three leaders. Ukraine and "
        "nuclear risks dominate the talks in Shenzhen.",
        font(SERIF, 22), 460, 28)
# three flag bars under the summit text
fx, fy = 32, 606
for i, col in enumerate([(178, 34, 34), (222, 200, 60), (30, 80, 160)]):
    d.rectangle([fx + i * 150, fy, fx + i * 150 + 132, fy + 30], fill=col,
                outline=INK, width=2)
d.text((32, 642), "USA  ·  CHINA  ·  RUSSIA", font=font(SANS_B, 19), fill=GREY)

d.line([512, 402, 512, 668], fill=RULE, width=2)
d.text((544, y), "WALL STREET  —  MARKETS", font=font(SANS_B, 21), fill=RED)
y3 = para(d, 544, y + 28, "STOCKS SLIDE AS AI", font(SERIF_B, 33), 448, 39)
y3 = para(d, 544, y3, "FEARS SPREAD", font(SERIF_B, 33), 448, 39)
y3 = para(d, 544, y3 + 4, "S&P 500 −2.0%, Nikkei −4.7%. Anthropic lists at a record "
        "$1.5 trillion — and still cannot calm the fall.",
        font(SERIF, 22), 448, 28)
# falling chart under the markets text
ox, oy = 544, 606
d.rectangle([ox, oy, ox + 448, oy + 60], outline=INK, width=2)
pts = [(ox + 8, oy + 12), (ox + 90, oy + 20), (ox + 170, oy + 16),
       (ox + 250, oy + 32), (ox + 330, oy + 42), (ox + 440, oy + 54)]
d.line(pts, fill=RED, width=5)
d.line([ox + 440, oy + 54, ox + 426, oy + 46], fill=RED, width=5)
d.line([ox + 440, oy + 54, ox + 426, oy + 58], fill=RED, width=5)
d.line([32, 688, 992, 688], fill=RULE, width=3)

# ---- third row: three stories ---------------------------------------------
y = 700
cols = [
    ("UKRAINE  —  WAR", "BRIDGE HIT AGAIN",
     "Ukraine hits the Crimea Bridge a third time in four days; the EU offers €45bn.", RED),
    ("GAZA  —  CEASEFIRE", "LINE CROSSED",
     "Israeli forces cross the “yellow line”; aid groups rate the peace plan 4 out of 26.", TEAL),
    ("ANTALYA  —  CLIMATE", "COP31 DEADLOCK",
     "Ministers meet late to unblock the climate talks as the summit in Turkey stalls.", GOLD),
]
cw = 304
for i, (kicker, head, body, col) in enumerate(cols):
    x = 32 + i * 328
    d.text((x, y), kicker, font=font(SANS_B, 19), fill=col)
    yy = para(d, x, y + 27, head, font(SERIF_B, 26), cw, 32)
    para(d, x, yy + 4, body, font(SERIF, 20), cw, 25)
    if i < 2:
        d.line([x + cw + 12, y, x + cw + 12, y + 128], fill=RULE, width=2)
d.line([32, 852, 992, 852], fill=RULE, width=3)

# ---- bottom ticker ---------------------------------------------------------
d.rectangle([0, 872, W, H], fill=NAVY)
d.text((32, 888), "ALSO ON 19 NOVEMBER 2026", font=font(SANS_B, 24), fill=(232, 196, 106))
para(d, 32, 922, "589 million children now live in conflict zones  ·  Denmark approves "
     "Greenland defence deal  ·  US Senate rejects Iran war-powers bid 51–48  ·  "
     "Van Gogh sells for $190.4m, an artist record  ·  Voyager 1 reaches one "
     "light-day from Earth", font(SANS, 22), 960, 30, color=(235, 235, 235))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
