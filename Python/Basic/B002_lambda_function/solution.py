nums = eval(input())

even = list(filter(lambda num: num % 2 == 0, nums))
odd = list(filter(lambda num: num % 2 != 0, nums))

print("Even numbers from the said list:")
print(even)

print("Odd numbers from the said list:")
print(odd)
