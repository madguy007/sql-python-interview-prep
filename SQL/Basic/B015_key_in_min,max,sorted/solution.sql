def closest_number(lst, k):
    diff = dict()

    for num in lst:
        diff[num] = abs(k - num)

    return min(diff, key=diff.get)


lst = [9, 11, 5, 3, 25, 18]
k = 6

print(closest_number(lst, k))