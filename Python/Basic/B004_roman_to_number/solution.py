# Roman to Integer Conversion

nums = input()

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

ans = 0

for i in range(len(nums)):
    if i < len(nums) - 1 and roman[nums[i]] < roman[nums[i + 1]]:
        ans = abs(ans - roman[nums[i]])
    else:
        ans += roman[nums[i]]

print(ans)