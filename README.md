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

## Stats *(as of June 2026 — updated manually, will be out of date)*

| Category        | Count   |
|-----------------|---------|
| Easy            | 160     |
| Medium          | 350     |
| Hard            | 115     |
| Meta problems   | 18      |
| Self challenges | 4       |
| **Total**       | **647** |

Files are typically named by LeetCode problem number and slug (for example `3742_max_path_score_in_a_grid.py`). Non-LeetCode problems use descriptive filenames.

## Tooling

- **Language:** Python 3.11+
- **Linter/formatter:** [Ruff](https://github.com/astral-sh/ruff)
- **Ruff config:** `pyproject.toml`

```bash
# Lint all Python files
ruff check python/

# Format all Python files
ruff format python/
```

## Notes

- Most LeetCode problems are from daily and weekly challenge cycles.
- Non-LeetCode problems are either learning exercises or interview prompt recommendations.
- The repository is intended as a living collection for practice and review.
