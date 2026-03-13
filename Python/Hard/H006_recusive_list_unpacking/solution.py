# Approach 1: Recursive solution (user approach)

nums = [1,[2,3],4,[5,[6,7]],8]

new_nums = list()

def number(nums):
    
    for num in nums:
        if type(num) == type([]):
            number(num)
        else:
            new_nums.append(num)

    return new_nums

print(number(nums))


# Approach 2: Cleaner recursive approach without global variable

nums = [1,[2,3],4,[5,[6,7]],8]

def flatten(nums):
    
    result = []
    
    for num in nums:
        if isinstance(num, list):
            result.extend(flatten(num))
        else:
            result.append(num)
    
    return result

print(flatten(nums))