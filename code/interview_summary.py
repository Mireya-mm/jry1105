#!/usr/bin/env python3
"""访谈记录汇总（示例脚本）。

读取 docs/02-访谈记录.csv，按角色汇总访谈要点。
用法：
    python interview_summary.py <path-to-csv>
"""
import csv
import sys
from collections import defaultdict


def summarize(csv_path):
    by_role = defaultdict(list)
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            by_role[row["interviewee_role"]].append(
                f"[{row['id']}] {row['interviewee_name']}: {row['key_view']}"
            )
    return by_role


def main():
    if len(sys.argv) < 2:
        print("用法: python interview_summary.py <path-to-csv>")
        sys.exit(1)
    by_role = summarize(sys.argv[1])
    for role, items in by_role.items():
        print(f"\n=== {role} ===")
        for it in items:
            print(f"  - {it}")


if __name__ == "__main__":
    main()
