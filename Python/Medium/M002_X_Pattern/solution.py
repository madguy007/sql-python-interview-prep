n = int(input())

s = 1
k = n

for m in range(n):
    for i in range(1, n + 1):
        if i == s or i == k:
            print('*', end="")
        else:
            print(' ', end="")
    print()
    s += 1
    k -= 1
