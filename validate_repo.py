"""Validate the interview-prep repository using only the standard library."""

from __future__ import annotations

import ast
import re
import subprocess
from pathlib import Path

from addq import DIFFICULTIES, LANGUAGES, render_readme


LINK_PATTERN = re.compile(r"\[Open\]\(([^)]+)\)")


def git_output(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def validate(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    question_paths: set[str] = set()
    question_count = 0

    for language in LANGUAGES:
        extension = "py" if language == "Python" else "sql"
        for difficulty in DIFFICULTIES:
            base = root / language / difficulty
            if not base.is_dir():
                errors.append(f"Missing difficulty directory: {base.relative_to(root)}")
                continue

            expected_prefix = difficulty[0].upper()
            seen_ids: set[str] = set()
            for folder in sorted(path for path in base.iterdir() if path.is_dir()):
                relative = folder.relative_to(root).as_posix()
                match = re.fullmatch(rf"({expected_prefix}\d{{3}})_(.+)", folder.name)
                if not match:
                    errors.append(f"Invalid question folder name: {relative}")
                    continue

                problem_id = match.group(1)
                if problem_id in seen_ids:
                    errors.append(f"Duplicate ID in {base.relative_to(root)}: {problem_id}")
                seen_ids.add(problem_id)
                question_count += 1
                question_paths.add(relative)

                expected_files = {"question.md", f"solution.{extension}", "insights.md"}
                actual_files = {path.name for path in folder.iterdir() if path.is_file()}
                missing = expected_files - actual_files
                unexpected = actual_files - expected_files
                if missing:
                    errors.append(f"{relative} is missing: {', '.join(sorted(missing))}")
                if unexpected:
                    errors.append(
                        f"{relative} has unexpected files: {', '.join(sorted(unexpected))}"
                    )

                for filename in expected_files & actual_files:
                    file_path = folder / filename
                    if not file_path.read_text(encoding="utf-8").strip():
                        errors.append(f"Empty file: {file_path.relative_to(root).as_posix()}")

                solution = folder / f"solution.{extension}"
                if language == "Python" and solution.exists():
                    try:
                        ast.parse(solution.read_text(encoding="utf-8"), filename=str(solution))
                    except SyntaxError as error:
                        errors.append(
                            f"Invalid Python syntax in {relative}/solution.py: {error.msg} "
                            f"(line {error.lineno})"
                        )

    readme = root / "README.md"
    if not readme.exists():
        errors.append("Missing README.md")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        readme_links = set(LINK_PATTERN.findall(readme_text))
        missing_links = question_paths - readme_links
        stale_links = readme_links - question_paths
        if missing_links:
            errors.append(f"README is missing {len(missing_links)} question link(s)")
        if stale_links:
            errors.append(f"README has {len(stale_links)} stale question link(s)")
        if readme_text != render_readme(root):
            errors.append("README.md is not synchronized with the repository structure")

    try:
        tracked_venv = git_output(root, "ls-files", "venv").strip()
        if tracked_venv:
            errors.append("venv/ is still tracked by Git")
        ignored = subprocess.run(
            [
                "git",
                "-c",
                f"safe.directory={root.as_posix()}",
                "check-ignore",
                "-q",
                "venv",
            ],
            cwd=root,
            check=False,
        )
        if ignored.returncode != 0:
            errors.append("venv/ is not ignored by Git")
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        errors.append(f"Could not validate Git configuration: {error}")

    return errors, question_count


def main() -> int:
    root = Path(__file__).resolve().parent
    errors, question_count = validate(root)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {question_count} questions successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
