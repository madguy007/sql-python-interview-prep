# -------- Approach 1 (Window technique similar to my original idea) --------

num = int(input())

l = num
r = num
gap = num - 1

for i in range(1, num+1):
    for j in range(1, num*2):
        if j < l or j > r:
            print(" ", end="")
        else:
            print(j-gap, end="")
    l -= 1
    r += 1
    gap -= 1
    print()

l = 2
r = 2*num - 2
gap = 1

for i in range(num-1, 0, -1):
    for j in range(1, num*2):
        if j < l or j > r:
            print(" ", end="")
        else:
            print(j-gap, end="")
    l += 1
    r -= 1
    gap += 1
    print()



# -------- Approach 2 (Cleaner solution using string multiplication) --------

num = int(input())

# upper half
for i in range(1, num+1):

    spaces = " " * (num-i)
    numbers = "".join(str(j) for j in range(1, 2*i))

    print(spaces + numbers + spaces)

# lower half
for i in range(num-1, 0, -1):

    spaces = " " * (num-i)
    numbers = "".join(str(j) for j in range(1, 2*i))

    print(spaces + numbers + spaces)