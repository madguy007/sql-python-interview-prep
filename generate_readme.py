import os

root = os.getcwd()

rows = []

for language in ["SQL", "Python"]:
    for difficulty in ["Basic", "Medium", "Hard"]:

        path = os.path.join(root, language, difficulty)

        if not os.path.exists(path):
            continue

        for folder in os.listdir(path):

            full = os.path.join(path, folder)

            if os.path.isdir(full):

                parts = folder.split("_",1)

                if len(parts) != 2:
                    continue

                pid = parts[0]
                name = parts[1]

                link = f"{language}/{difficulty}/{folder}"

                rows.append((pid,language,difficulty,name,link))


rows.sort()

readme = "# SQL & Python Interview Prep\n\n"
readme += "| ID | Language | Difficulty | Problem | Link |\n"
readme += "|----|----------|-----------|--------|------|\n"

for r in rows:
    readme += f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | [Open]({r[4]}) |\n"

with open("README.md","w",encoding="utf8") as f:
    f.write(readme)

print("README generated successfully")