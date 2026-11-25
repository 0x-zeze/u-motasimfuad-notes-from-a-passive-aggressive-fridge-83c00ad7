# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/0x-zeze/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/0x-zeze/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

A passive-aggressive fridge note, written by the fridge itself. It found your leftovers in 0.4 seconds — and it knows exactly where your keys are. It is not helping.

## The entry

> My sensors found the leftovers behind the pickles in 0.4 seconds. Your keys have been missing for three days. I know exactly where they are.

The note is 140 characters. The joke lands in three beats: the fridge brags about its sensors, it pivots to your missing keys, and it ends on a smug refusal to help — the grudge is the punchline.

## How it works

`main.py` writes the note to `/output/entry.txt` as UTF-8 text. The output is deterministic: the same 140-character note on every run.

## Run it

```sh
python main.py
cat /output/entry.txt
```
