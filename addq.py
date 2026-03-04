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
print("Press ENTER twice when done\n")

print("Paste everything now. Finish by typing END on a new line.\n")

lines = []
while True:
    line = input()
    if line.strip() == "END":
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

question = content[q_start+13:s_start].strip()
solution = content[s_start+13:i_start].strip()
insights = content[i_start+13:].strip()

base = os.path.join(language, difficulty)

folders = [f for f in os.listdir(base) if os.path.isdir(os.path.join(base, f))]
num = len(folders) + 1

prefix = difficulty[0].upper()
number = f"{prefix}{num:03d}"

folder_name = f"{number}_{name}"
path = os.path.join(base, folder_name)

os.makedirs(path)

with open(os.path.join(path, "question.md"), "w") as f:
    f.write(question)

ext = "sql" if language.lower() == "sql" else "py"

with open(os.path.join(path, f"solution.{ext}"), "w") as f:
    f.write(solution)

with open(os.path.join(path, "insights.md"), "w") as f:
    f.write(insights)

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Added {folder_name}"])
subprocess.run(["git", "push"])

print(f"\n✅ Problem stored: {folder_name}")