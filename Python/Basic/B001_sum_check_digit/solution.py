'''manual counting code '''

num1 = int(input())
num2 = int(input())

def count_digit(num):
    num = abs(num)
    count = 0
    while num:
        num = num // 10
        count += 1
    return count

if count_digit(num1) > 80 or count_digit(num2)>80:
    print("Overflow!")
else:
    print(num1+num2)


''' simple method'''
if len(str(abs(num1))) > 80 or len(str(abs(num2))) > 80:
    print("Overflow!")
else:
    print(num1 + num2)
