# Approach 1: User Solution (building pattern step by step)

num = 5
n = 2*num-1
count = 0
t = n

pattern = f'{num}'*n
print(pattern)

# upper part
for i in range(1,num):
    count +=  1
    t -= 2
    
    start = pattern[:count] 
    mid = f"{num-i}"*t
    end = pattern[n-count:]
    
    pattern = start + mid + end

    print(pattern)

# lower part
for i in range(num-2, -1, -1):
    count -= 1
    t += 2
    
    start = pattern[:count]
    mid = f"{num-i}" * t
    end = pattern[n-count:]
    
    pattern = start + mid + end
    print(pattern)



# Approach 2: Mathematical Solution (Simpler)

num = int(input())
n = 2*num - 1

for i in range(n):
    for j in range(n):
        val = num - min(i, j, n-1-i, n-1-j)
        print(val, end="")
    print()