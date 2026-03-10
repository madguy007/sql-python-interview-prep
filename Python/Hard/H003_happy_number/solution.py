def happy_number():
    num = int(input())
    temp = num
    counter = 0
    
    while temp != 1:
        total = 0
        counter += 1
        if counter < 5:  
            while temp:
                digit = temp % 10
                total += digit ** 2
                temp = temp // 10
            temp = total
        else:
            return False
    return True    
    
print(happy_number())