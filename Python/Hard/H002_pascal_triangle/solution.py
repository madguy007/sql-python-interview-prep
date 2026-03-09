def pascal_triangle():
    num = int(input())
    triangle = list()

    for i in range(num):
        num_tri = list()

        for j in range(i + 1):

            # First and last elements are always 1
            if j == 0 or j == i:
                num_tri.append(1)

            else:
                mid_ele = triangle[i-1][j-1] + triangle[i-1][j]
                num_tri.append(mid_ele)

        triangle.append(num_tri)

    return triangle


print(pascal_triangle())