nums = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7

pairs = set()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.add(tuple(sorted((nums[i], nums[j]))))

print(list(pairs))