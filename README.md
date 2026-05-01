# LeetCodeProblems

This repo upon it's creation was just for leet code problems.
Over time it turned into generic interview prep solutions.
It would more aptly be named: **InterviewPrepProblems**

Leet code ones are mostly from the daily and weekly challenges.
Non Leet code ones are either things I wanted to learn or suggestions from companies.

---

## Structure

```text
python/
├── easy/           # LeetCode easy problems
├── medium/         # LeetCode medium problems
├── hard/           # LeetCode hard problems
├── meta_problems/  # Meta/Facebook interview problems (leveled variants)
└── self_challenges/# Self-directed problems and data structure implementations
```

## Stats *(as of May 2026 — updated manually, will be out of date)*

| Category        | Count   |
|-----------------|---------|
| Easy            | 146     |
| Medium          | 319     |
| Hard            | 102     |
| Meta problems   | 18      |
| Self challenges | 4       |
| **Total**       | **589** |

Files are named by LeetCode problem number and slug (e.g. `3742_max_path_score_in_a_grid.py`), or descriptively for non-LeetCode problems (e.g. `boss_fight_level_3.py`).

## Tooling

- **Language:** Python 3.11+
- **Linter/formatter:** [Ruff](https://github.com/astral-sh/ruff) — config in `pyproject.toml`

```bash
# Lint
ruff check python/

# Format
ruff format python/
```
