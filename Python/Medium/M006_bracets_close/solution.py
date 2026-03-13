# Approach 1: Stack approach (user solution)

brac = input()
new = []

close = {')': '('}

for b in brac:
    flag = 1
    if b not in close:
        new.append(b)
    else:
        if len(new) == 0 and b == ')':
            flag = 0
            break
        else:
            new.pop()

if len(new) == 0 and flag == 1:
    print(True)
else:
    print(False)



# Approach 2: Shorter stack solution

brac = input()
stack = []

for b in brac:
    if b == '(':
        stack.append(b)
    else:
        if not stack:
            print(False)
            break
        stack.pop()
else:
    print(len(stack) == 0)