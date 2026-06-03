### Method - 01 - double loop

nums = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7

pairs = set()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.add(tuple(sorted((nums[i], nums[j]))))

print(list(pairs))


### Method - 02 - one loop 
def unique_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        remain = target - num

        if remain in seen:
            pairs.add(tuple(sorted((num, remain))))

        seen.add(num)

    return list(pairs)


nums = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7

print(unique_pairs(nums, target))
