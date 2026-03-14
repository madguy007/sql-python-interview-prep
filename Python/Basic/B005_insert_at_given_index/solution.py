nums = eval(input())
index = eval(input())

target = []

for i in range(len(nums)):
    target.insert(index[i], nums[i])

print(target)