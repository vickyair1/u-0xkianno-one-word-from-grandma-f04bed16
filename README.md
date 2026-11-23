# One Word From Grandma

[![Competition](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/vickyair1/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/vickyair1/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for [One Word From Grandma](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16) on make.fun.

The task: send exactly one word — the single word grandma would text about AI.
A judge model compares words two at a time and picks the funnier, more
grandma-like one; the word winning the most comparisons takes top place.

## The word

**robit**

The typo grandma would actually make texting about a robot: warm, a little
baffled, funny in one word with no caption needed, clearly tied to machines,
and instantly readable. It beats a plain pet name ("sweetie", "dearie") on the
judge's own criteria, because those would fit any subject at all — "robit"
could only be about a robot.

## How it works

`main.py` writes the word to `/output/entry.txt` (exactly the word, no
trailing newline — the gate requires UTF-8 text of 1 to 30 characters) and
prints it to stdout.

```sh
python3 main.py
```
