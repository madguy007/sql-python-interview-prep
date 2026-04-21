s = "abciiidef"
k = 3
vowels = {'a','e','i','o','u'}

# first window
count = 0
for i in range(k):
    if s[i] in vowels:
        count += 1

max_v = count

# slide window
for i in range(k, len(s)):
    if s[i] in vowels:        # add new
        count += 1
    if s[i-k] in vowels:      # remove old
        count -= 1
        
    max_v = max(max_v, count)

print(max_v)