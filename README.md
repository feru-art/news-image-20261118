# Wednesday 18 November 2026 — in one image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/feru-art/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/feru-art/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for the [make.fun bounty](https://make.fun/bounty/news-image-20261118):
sum up 18 November's world news in one image.

The image is a six-panel front page for **Wednesday 18 November 2026**:

- **Trump in Manila** — the US president arrives in the Philippines
- **Crimea Bridge Hit** — Ukraine strikes the Kerch bridge, day two
- **Gulf Clash** — drones and warships around the Strait of Hormuz
- **Cyclone Akvan** — the storm over the Bay of Bengal
- **UK Sanctions** — Britain sanctions firms tied to Israeli settlements
- **Dhoni Retires** — MS Dhoni retires from the IPL to mentor Chennai

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies the shipped `image.jpg` (JPEG bytes, 201,317 bytes,
1024×683) to `/output/entry.png` after checking it against the
competition's limits (≤1 MiB, ≤1024×1024). The file is a JPEG told apart
by its first bytes; the name stays `entry.png` either way, per RULES.txt.
