text = "abcabcd"

subs = []
s = ""

for ch in text:
    if ch not in s:
        s += ch
    else:
        subs.append(s)
        s = ch

subs.append(s)   # add last substring

print(subs)

print(len(max(subs)))