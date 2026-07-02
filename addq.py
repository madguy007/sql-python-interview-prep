"""Interactive helper for adding SQL and Python revision questions."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Callable


LANGUAGES = ("Python", "SQL")
DIFFICULTIES = ("Basic", "Medium", "Hard")
MARKER_PATTERN = re.compile(
    r"^\s*===(QUESTION|SOLUTION|INSIGHTS)===\s*$", re.IGNORECASE | re.MULTILINE
)


class InputError(ValueError):
    """Raised when pasted question content is invalid."""


def parse_content(content: str) -> tuple[str, str, str]:
    """Return question, solution, and insights from the marked input."""
    markers = list(MARKER_PATTERN.finditer(content))
    expected = ["question", "solution", "insights"]
    found = [match.group(1).lower() for match in markers]

    if found != expected:
        raise InputError(
            "Use each marker once and in this order: "
            "===QUESTION===, ===SOLUTION===, ===INSIGHTS==="
        )

    sections = []
    for index, marker in enumerate(markers):
        start = marker.end()
        end = markers[index + 1].start() if index + 1 < len(markers) else len(content)
        sections.append(content[start:end].strip())

    empty = [name for name, value in zip(expected, sections) if not value]
    if empty:
        raise InputError(f"These sections cannot be empty: {', '.join(empty)}")

    return sections[0], sections[1], sections[2]


def normalize_problem_name(name: str) -> str:
    """Create a safe, readable folder-name suffix."""
    normalized = re.sub(r"\s+", "_", name.strip())
    normalized = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", normalized)
    normalized = normalized.rstrip(". ")
    if not normalized or normalized in {".", ".."}:
        raise InputError("Problem name must contain at least one valid character")
    return normalized


def next_problem_id(base: Path, difficulty: str) -> str:
    """Find the next ID from the highest existing numeric ID."""
    prefix = difficulty[0].upper()
    highest = 0
    pattern = re.compile(rf"^{prefix}(\d+)_")

    if base.exists():
        for folder in base.iterdir():
            if folder.is_dir() and (match := pattern.match(folder.name)):
                highest = max(highest, int(match.group(1)))

    return f"{prefix}{highest + 1:03d}"


def collect_questions(root: Path) -> dict[str, list[tuple[str, str, str, str]]]:
    """Collect README rows in language and difficulty order."""
    questions: dict[str, list[tuple[str, str, str, str]]] = {}
    for language in LANGUAGES:
        rows = []
        for difficulty in DIFFICULTIES:
            base = root / language / difficulty
            if not base.exists():
                continue
            for folder in sorted(base.iterdir()):
                if not folder.is_dir() or "_" not in folder.name:
                    continue
                problem_id, problem_name = folder.name.split("_", 1)
                link = folder.relative_to(root).as_posix()
                rows.append((problem_id, difficulty, problem_name, link))
        questions[language] = rows
    return questions


def render_readme(root: Path) -> str:
    """Generate the complete README, including stable documentation."""
    questions = collect_questions(root)
    python_count = len(questions["Python"])
    sql_count = len(questions["SQL"])
    total = python_count + sql_count

    lines = [
        "# SQL & Python Interview Prep",
        "",
        "A personal revision bank of interview questions, solutions, and learning insights,",
        "organized by language and difficulty.",
        "",
        "## Progress",
        "",
        "| Language | Questions |",
        "|----------|-----------|",
        f"| Python | {python_count} |",
        f"| SQL | {sql_count} |",
        f"| **Total** | **{total}** |",
        "",
        "## Adding a question",
        "",
        "Run `addq.bat` on Windows or `python addq.py`, choose the language and difficulty,",
        "then paste the content in this format:",
        "",
        "```text",
        "===QUESTION===",
        "Your question",
        "===SOLUTION===",
        "Your solution",
        "===INSIGHTS===",
        "Your revision notes",
        "MADDY",
        "```",
        "",
        "Each problem is stored as `question.md`, `solution.py` or `solution.sql`, and",
        "`insights.md`. The helper asks before committing and pushing to GitHub.",
        "",
        "> SQL solutions use a mixture of MySQL, PostgreSQL, and SQLite syntax. Check each",
        "> question and solution for dialect-specific notes.",
        "",
    ]

    for language in LANGUAGES:
        lines.extend(
            [
                f"## {language} Questions",
                "",
                "| ID | Difficulty | Problem | Link |",
                "|----|------------|---------|------|",
            ]
        )
        for problem_id, difficulty, problem_name, link in questions[language]:
            lines.append(
                f"| {problem_id} | {difficulty} | {problem_name} | [Open]({link}) |"
            )
        lines.append("")

    return "\n".join(lines)


def create_question(
    root: Path,
    language: str,
    difficulty: str,
    name: str,
    content: str,
) -> Path:
    """Validate input, create the question folder, and refresh the README."""
    question, solution, insights = parse_content(content)
    safe_name = normalize_problem_name(name)
    base = root / language / difficulty
    base.mkdir(parents=True, exist_ok=True)
    problem_id = next_problem_id(base, difficulty)
    folder = base / f"{problem_id}_{safe_name}"

    if folder.exists():
        raise InputError(f"Folder already exists: {folder.name}")

    folder.mkdir()
    (folder / "question.md").write_text(question + "\n", encoding="utf-8")
    extension = "sql" if language == "SQL" else "py"
    (folder / f"solution.{extension}").write_text(solution + "\n", encoding="utf-8")
    (folder / "insights.md").write_text(insights + "\n", encoding="utf-8")
    (root / "README.md").write_text(render_readme(root), encoding="utf-8")
    return folder


def run_git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Run Git and raise a readable error when it fails."""
    return subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )


def publish_question(
    root: Path,
    folder: Path,
    git_runner: Callable[..., subprocess.CompletedProcess[str]] = run_git,
) -> None:
    """Commit only generated files, rebase safely, and push the current branch."""
    relative_folder = folder.relative_to(root).as_posix()

    status_result = git_runner(root, "status", "--porcelain", "--untracked-files=all")
    unrelated = []
    for line in status_result.stdout.splitlines():
        changed_path = line[3:].replace("\\", "/")
        if changed_path != "README.md" and not changed_path.startswith(
            relative_folder + "/"
        ):
            unrelated.append(changed_path)
    if unrelated:
        raise RuntimeError(
            "Commit or stash unrelated changes before publishing: "
            + ", ".join(unrelated)
        )

    branch_result = git_runner(root, "branch", "--show-current")
    branch = branch_result.stdout.strip()
    if not branch:
        raise RuntimeError("Cannot publish from a detached HEAD")

    git_runner(root, "add", "--", relative_folder, "README.md")
    git_runner(root, "commit", "-m", f"Add {folder.name}")
    git_runner(root, "pull", "--rebase", "origin", branch)
    git_runner(root, "push", "origin", branch)


def choose(
    prompt: str,
    choices: dict[str, str],
    input_fn: Callable[[str], str],
) -> str:
    value = input_fn(prompt).strip().lower()
    if value not in choices:
        raise InputError(f"Choose one of: {', '.join(choices)}")
    return choices[value]


def main(
    root: Path | None = None,
    input_fn: Callable[[str], str] = input,
    output: Callable[[str], None] = print,
) -> int:
    root = Path.cwd() if root is None else root

    try:
        language = choose(
            "Language (SQL/Python): ", {"sql": "SQL", "python": "Python"}, input_fn
        )
        difficulty = choose(
            "Difficulty (Basic/Medium/Hard): ",
            {item.lower(): item for item in DIFFICULTIES},
            input_fn,
        )
        name = input_fn("Problem name: ")

        output("\nPaste content using markers:")
        output("===QUESTION===")
        output("===SOLUTION===")
        output("===INSIGHTS===")
        output("\nPaste everything now. Finish by typing MADDY on a new line.\n")

        lines = []
        while True:
            line = input_fn("")
            if line.strip() == "MADDY":
                break
            lines.append(line)

        folder = create_question(root, language, difficulty, name, "\n".join(lines))
        output(f"\nProblem stored: {folder.name}")

        publish = input_fn("Commit and push this question to GitHub now? (y/N): ")
        if publish.strip().lower() not in {"y", "yes"}:
            output("Saved locally. Nothing was committed or pushed.")
            return 0

        try:
            publish_question(root, folder)
        except (subprocess.CalledProcessError, RuntimeError) as error:
            details = getattr(error, "stderr", "") or str(error)
            output(f"Git publication stopped: {details.strip()}")
            output("Your question remains saved locally; no force-push was attempted.")
            return 1

        output("Committed and pushed successfully.")
        return 0
    except (InputError, EOFError, KeyboardInterrupt) as error:
        output(f"Error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
