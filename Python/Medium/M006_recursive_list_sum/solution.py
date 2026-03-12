# Approach 1: Recursive solution (user approach)

nums = eval(input())

def list_sum(nums):
    total = 0
    
    for num in nums:
        if type(num) == type([]):
            total = total + list_sum(num)
        else:
            total += num
            
    return total

print(list_sum(nums))


# Approach 2: Cleaner recursive approach using isinstance()

nums = eval(input())

def list_sum(nums):
    total = 0
    
    for num in nums:
        if isinstance(num, list):
            total += list_sum(num)
        else:
            total += num
            
    return total

print(list_sum(nums))