def base_13(num):
    sign = ""

    # Handle negative numbers
    if num < 0:
        sign = '-'
        num = abs(num)

    # Mapping for 10, 11, 12
    dic = {
        10: 'A',
        11: 'B',
        12: 'C'
    }

    # Base cases
    if num < 10:
        return sign + str(num)

    elif num < 13:
        return sign + dic[num]

    # Recursive conversion
    remainder = num % 13
    quotient = num // 13

    return (
        sign
        + base_13(quotient)
        + (str(remainder) if remainder < 10 else dic[remainder])
    )


# Test Cases
print(base_13(49))   # 3A
print(base_13(69))   # 54
print(base_13(13))   # 10
print(base_13(-49))  # -3A