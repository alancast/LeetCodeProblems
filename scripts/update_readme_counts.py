#!/usr/bin/env python3
"""Update the README problem counts from the current python/ directory.

Usage:
  python3 scripts/update_readme_counts.py
  python3 scripts/update_readme_counts.py --dry-run
"""

from __future__ import annotations

import argparse
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
PYTHON_ROOT = REPO_ROOT / "python"

CATEGORIES: list[tuple[str, str]] = [
    ("Easy", "easy"),
    ("Medium", "medium"),
    ("Hard", "hard"),
    ("Meta problems", "meta_problems"),
    ("Self challenges", "self_challenges"),
]

# Matches the stats heading then the entire markdown table that follows it.
TABLE_BLOCK_PATTERN = re.compile(
    r"(## Stats[^\n]*\n\n)"
    r"(\| Category.*?\n\|[-|]+\n(?:\|.*?\n)+)",
    re.MULTILINE,
)


def count_problem_files() -> dict[str, int]:
    if not PYTHON_ROOT.exists():
        raise FileNotFoundError(f"Python folder not found: {PYTHON_ROOT}")

    counts: dict[str, int] = {}
    for label, folder in CATEGORIES:
        folder_path = PYTHON_ROOT / folder
        if not folder_path.exists():
            counts[label] = 0
            continue
        counts[label] = sum(
            1
            for entry in folder_path.iterdir()
            if entry.is_file() and entry.suffix == ".py"
        )
    return counts


def format_count_table(counts: dict[str, int]) -> str:
    total = sum(counts.values())
    total_label = "**Total**"
    total_count_str = f"**{total}**"

    data_rows = [(label, str(counts[label])) for label, _ in CATEGORIES]

    cat_w = max(len("Category"), *(len(r) for r, _ in data_rows), len(total_label))
    cnt_w = max(len("Count"), *(len(c) for _, c in data_rows), len(total_count_str))

    header    = f"| {'Category':<{cat_w}} | {'Count':<{cnt_w}} |"
    separator = f"|{'-' * (cat_w + 2)}|{'-' * (cnt_w + 2)}|"
    rows      = [f"| {label:<{cat_w}} | {cnt:<{cnt_w}} |" for label, cnt in data_rows]
    total_row = f"| {total_label:<{cat_w}} | {total_count_str:<{cnt_w}} |"

    return "\n".join([header, separator, *rows, total_row]) + "\n"


def update_readme(counts: dict[str, int], dry_run: bool = False) -> None:
    text = README_PATH.read_text()
    match = TABLE_BLOCK_PATTERN.search(text)
    if not match:
        raise RuntimeError("Could not find the README stats table to update.")

    new_table = format_count_table(counts)

    if dry_run:
        print("README counts would be updated to:")
        print(new_table)
        return

    new_text = text[: match.start(2)] + new_table + text[match.end(2) :]
    README_PATH.write_text(new_text)
    print(f"Updated README counts in {README_PATH}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update README problem counts from python/ directories.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the updated table without writing to README.md",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    counts = count_problem_files()
    update_readme(counts, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
