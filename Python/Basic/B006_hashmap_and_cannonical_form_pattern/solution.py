arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

group = dict()

for word in arr:
    key = "".join(sorted(word))
    if key not in group:
        group[key] = []
    group[key].append(word)

print(list(group.values()))