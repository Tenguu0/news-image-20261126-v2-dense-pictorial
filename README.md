# The World in One Page — Thursday 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Tenguu0/news-image-20261126-v2-dense-pictorial/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Tenguu0/news-image-20261126-v2-dense-pictorial/reward.svg)](https://make.fun/bounty/news-image-20261126)

An entry for the [news-image-20261126 bounty](https://make.fun/bounty/news-image-20261126): one 1024×1024 newspaper front page that sums up Thursday 26 November 2026 — the dense, fully pictured format. A big illustrated lead story, twelve illustrated stories in a 4×3 grid, and an ALSO TODAY strip of lighter items at the bottom. Every picture is an AI-generated illustration, not a photograph of the events.

## How to run

You need Python 3 and Pillow:

```sh
pip install pillow
```

Then, from this directory, run:

```sh
python3 main.py
```

The script reads the pictures from `assets/`, draws the complete page with Pillow (using the DejaVu fonts bundled in `assets/fonts/`), and writes `entry.png` beside `main.py`. To put the output somewhere else, set `MAKEFUN_OUTPUT_DIR` before running:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It needs no network access while it runs — every picture and every word is already in this repository. The render is deterministic: running it three times produces byte-identical `entry.png` files.

## What's in the news

**Lead — Middle East / Oil:** Yemen's Houthis said they attacked Saudi Arabia's Ras Tanura refinery and Riyadh's financial district; Saudi forces said they shot down four drones over Ras Tanura. Brent crude settled 3.5% higher at $94.61 a barrel.

**The grid (12 stories):**

1. **Strait of Hormuz** — Two oil tankers hit naval mines in the strait.
2. **Gaza** — Israel kills Hamas security chief Mohammad Abuelouf in Gaza.
3. **Ukraine** — Ukraine hits two Russian oil refineries overnight.
4. **Space** — First Pakistani astronaut, Muhammad Zeeshan Ali, heads to China's Tiangong station on Shenzhou-24.
5. **Trade** — US proposes tariffs of up to 15% on Taiwan goods.
6. **Science** — ESA's Hera reveals a stadium-size crater on asteroid Dimorphos, left by NASA's 2022 DART impact.
7. **Chess** — Gukesh draws Game 2 of the World Chess Championship against Javokhir Sindarov.
8. **Cricket** — Vaibhav Sooryavanshi, 15, smashes a record List A double century (204 off 53 balls).
9. **India** — India marks Constitution Day and the 18th anniversary of the 26/11 Mumbai attacks.
10. **Bangladesh** — Bangladesh raises the garment minimum wage by 36%.
11. **Economy** — The Fed's Beige Book: modest growth, wage gains, persistent price pressure.
12. **Egypt** — A fuel tanker crash fire on a highway around Cairo kills at least 30 people.

**Also today:** IPL 2027 auction draws 1,220 players; Solomon Islands and Australia sign a security treaty; North Korea orders the Swiss office in Pyongyang shut; Duran Duran guitarist Andy Taylor dies at 65.

## Sources

Reuters, ESA, BBC and wire reports from 26 November 2026. Figures are reported as claimed or as officially stated — the Houthi attack claim was not independently confirmed at the time of writing.
