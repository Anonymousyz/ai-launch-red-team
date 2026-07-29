from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        raise SystemExit(f"missing public file: {path}")
    return target.read_text(encoding="utf-8")


def main() -> None:
    chinese = require("README.md")
    english = require("README.en.md")
    skill = require("SKILL.md")
    status = require("STATUS.md")

    if "STATUS.md" not in chinese or "STATUS.md" not in english:
        raise SystemExit("both READMEs must link to STATUS.md")
    if "8" not in skill or "eight" not in english.lower():
        raise SystemExit("public documentation must state the review-card scope consistently")
    if "不替代什么" not in status:
        raise SystemExit("STATUS.md must state what the skill does not replace")

    print("OK: public documentation surface is complete")


if __name__ == "__main__":
    main()
