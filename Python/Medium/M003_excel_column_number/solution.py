def excel_col_num():
    columnTitle = input().upper()

    num = 0

    for ch in columnTitle:
        num = num * 26 + (ord(ch) - ord('A') + 1)

    return num


print(excel_col_num())