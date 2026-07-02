from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import addq


VALID_CONTENT = """===QUESTION===
What is the answer?
===SOLUTION===
print(42)
===INSIGHTS===
Validate before publishing.
"""


class AddQuestionTests(unittest.TestCase):
    def make_root(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        for language in addq.LANGUAGES:
            for difficulty in addq.DIFFICULTIES:
                (root / language / difficulty).mkdir(parents=True)
        return temporary, root

    def test_parse_content_requires_ordered_nonempty_markers(self) -> None:
        self.assertEqual(
            addq.parse_content(VALID_CONTENT),
            ("What is the answer?", "print(42)", "Validate before publishing."),
        )
        with self.assertRaises(addq.InputError):
            addq.parse_content("===SOLUTION===\nx\n===QUESTION===\ny\n===INSIGHTS===\nz")
        with self.assertRaises(addq.InputError):
            addq.parse_content("===QUESTION===\n\n===SOLUTION===\nx\n===INSIGHTS===\ny")
        with self.assertRaises(addq.InputError):
            addq.parse_content("===QUESTION===\nx\n===SOLUTION===\ny")

    def test_next_id_uses_highest_number_when_there_is_a_gap(self) -> None:
        temporary, root = self.make_root()
        with temporary:
            base = root / "Python" / "Medium"
            (base / "M001_first").mkdir()
            (base / "M003_third").mkdir()
            self.assertEqual(addq.next_problem_id(base, "Medium"), "M004")

    def test_create_python_and_sql_questions(self) -> None:
        temporary, root = self.make_root()
        with temporary:
            python_folder = addq.create_question(
                root, "Python", "Medium", "python sample", VALID_CONTENT
            )
            sql_folder = addq.create_question(
                root,
                "SQL",
                "Hard",
                "sql sample",
                VALID_CONTENT.replace("print(42)", "SELECT 42;"),
            )
            self.assertTrue((python_folder / "solution.py").exists())
            self.assertTrue((sql_folder / "solution.sql").exists())
            self.assertIn("**Total** | **2**", (root / "README.md").read_text())

    def test_current_interactive_flow_can_decline_publication(self) -> None:
        temporary, root = self.make_root()
        with temporary:
            responses = iter(
                [
                    "python",
                    "medium",
                    "interactive sample",
                    "===QUESTION===",
                    "Question",
                    "===SOLUTION===",
                    "print(1)",
                    "===INSIGHTS===",
                    "Insight",
                    "MADDY",
                    "n",
                ]
            )
            output: list[str] = []
            result = addq.main(root, lambda _prompt: next(responses), output.append)
            self.assertEqual(result, 0)
            self.assertTrue((root / "Python" / "Medium" / "M001_interactive_sample").exists())
            self.assertIn("Saved locally. Nothing was committed or pushed.", output)

    def test_accepting_publication_calls_safe_git_workflow(self) -> None:
        temporary, root = self.make_root()
        with temporary:
            folder = addq.create_question(root, "Python", "Basic", "publish", VALID_CONTENT)
            calls: list[tuple[str, ...]] = []

            def fake_git(_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
                calls.append(args)
                stdout = "main\n" if args == ("branch", "--show-current") else ""
                return subprocess.CompletedProcess(["git", *args], 0, stdout, "")

            addq.publish_question(root, folder, fake_git)
            self.assertEqual(
                calls,
                [
                    ("status", "--porcelain", "--untracked-files=all"),
                    ("branch", "--show-current"),
                    ("add", "--", "Python/Basic/B001_publish", "README.md"),
                    ("commit", "-m", "Add B001_publish"),
                    ("pull", "--rebase", "origin", "main"),
                    ("push", "origin", "main"),
                ],
            )

    def test_publication_rejects_unrelated_changes(self) -> None:
        temporary, root = self.make_root()
        with temporary:
            folder = addq.create_question(root, "Python", "Basic", "publish", VALID_CONTENT)

            def fake_git(_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
                stdout = " M unrelated.txt\n" if args[0] == "status" else ""
                return subprocess.CompletedProcess(["git", *args], 0, stdout, "")

            with self.assertRaisesRegex(RuntimeError, "unrelated.txt"):
                addq.publish_question(root, folder, fake_git)

    def test_interactive_yes_uses_publication_function(self) -> None:
        temporary, root = self.make_root()
        with temporary:
            responses = iter(
                [
                    "sql",
                    "basic",
                    "publish sample",
                    "===QUESTION===",
                    "Question",
                    "===SOLUTION===",
                    "SELECT 1;",
                    "===INSIGHTS===",
                    "Insight",
                    "MADDY",
                    "yes",
                ]
            )
            with patch("addq.publish_question") as publish:
                result = addq.main(root, lambda _prompt: next(responses), lambda _line: None)
            self.assertEqual(result, 0)
            publish.assert_called_once()


if __name__ == "__main__":
    unittest.main()
