import os
import subprocess

language = input("Language (SQL/Python): ").strip()
difficulty = input("Difficulty (Basic/Medium/Hard): ").strip()
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

question = content.split("===SOLUTION===")[0].replace("===QUESTION===", "").strip()
solution = content.split("===SOLUTION===")[1].split("===INSIGHTS===")[0].strip()
insights = content.split("===INSIGHTS===")[1].strip()

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