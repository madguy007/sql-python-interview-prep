import os
import subprocess

language = input("Language (SQL/Python): ").strip().lower()

if language not in ["sql", "python"]:
    print("❌ Language must be SQL or Python")
    exit()

language = "SQL" if language == "sql" else "Python"

difficulty = input("Difficulty (Basic/Medium/Hard): ").strip().lower()

if difficulty not in ["basic", "medium", "hard"]:
    print("❌ Difficulty must be Basic, Medium, or Hard")
    exit()

difficulty = difficulty.capitalize()

name = input("Problem name: ").strip().replace(" ", "_")

print("\nPaste content using markers:")
print("===QUESTION===")
print("===SOLUTION===")
print("===INSIGHTS===")

print("Paste everything now. Finish by typing MADDY on a new line.\n")

lines = []
while True:
    line = input()
    if line.strip() == "MADDY":
        break
    lines.append(line)

content = "\n".join(lines)

content_lower = content.lower()

q_start = content_lower.find("===question===")
s_start = content_lower.find("===solution===")
i_start = content_lower.find("===insights===")

if q_start == -1 or s_start == -1 or i_start == -1:
    print("❌ Missing markers. Use ===QUESTION===, ===SOLUTION===, ===INSIGHTS===")
    exit()

question = content[q_start+len("===question==="):s_start].strip()
solution = content[s_start+len("===solution==="):i_start].strip()
insights = content[i_start+len("===insights==="):].strip()

base = os.path.join(language, difficulty)

folders = [f for f in os.listdir(base) if os.path.isdir(os.path.join(base, f))]
num = len(folders) + 1

prefix = difficulty[0].upper()
number = f"{prefix}{num:03d}"

folder_name = f"{number}_{name}"
path = os.path.join(base, folder_name)

if os.path.exists(path):
    print("❌ Folder already exists:", folder_name)
    exit()

os.makedirs(path)

with open(os.path.join(path, "question.md"), "w", encoding="utf8") as f:
    f.write(question)

ext = "sql" if language.lower() == "sql" else "py"

with open(os.path.join(path, f"solution.{ext}"), "w", encoding="utf8") as f:
    f.write(solution)

with open(os.path.join(path, "insights.md"), "w", encoding="utf8") as f:
    f.write(insights)

# Generate README content with separate tables
readme = "# SQL & Python Interview Prep\n\n"

for lang in ["Python", "SQL"]:
    readme += f"## {lang} Questions\n"
    readme += "| ID | Difficulty | Problem | Link |\n"
    readme += "|----|-----------|---------|------|\n"

    # Gather all rows for this specific language
    lang_rows = []
    for diff in ["Basic", "Medium", "Hard"]:
        p = os.path.join(lang, diff)
        if not os.path.exists(p):
            continue

        for folder in os.listdir(p):
            full = os.path.join(p, folder)
            if os.path.isdir(full):
                parts = folder.split("_", 1)
                if len(parts) != 2:
                    continue
                pid, pname = parts[0], parts[1]
                link = f"{lang}/{diff}/{folder}"
                lang_rows.append((pid, diff, pname, link))

    # Sort by ID
    lang_rows.sort()

    for r in lang_rows:
        readme += f"| {r[0]} | {r[1]} | {r[2]} | [Open]({r[3]}) |\n"

    readme += "\n"

with open("README.md", "w", encoding="utf8") as f:
    f.write(readme)

print("README updated")

subprocess.run(["git", "pull", "origin", "main", "--rebase"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Added {folder_name}"])
subprocess.run(["git", "push"])

print(f"\n✅ Problem stored: {folder_name}")
