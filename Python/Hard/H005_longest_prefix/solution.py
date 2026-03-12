# Approach 1: User's approach using sorting

words = eval(input())
words.sort()

short = len(words[0])
for word in words:
    if len(word) < short:
        short = len(word)

first = words[0]
last = words[-1]
prefix = ""

for i in range(short):
    if first[i] == last[i]:
        prefix += last[i]
    else:
        break

print(prefix)



# Approach 2: Shorter approach using zip()

words = eval(input())
words.sort()

first = words[0]
last = words[-1]

prefix = ""

for a, b in zip(first, last):
    if a == b:
        prefix += a
    else:
        break

print(prefix)