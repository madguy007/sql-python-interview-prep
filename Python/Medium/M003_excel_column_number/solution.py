def excel_col_num():
    columnTitle = input().upper()

    num = 0

    for ch in columnTitle:
        num = num * 26 + (ord(ch) - ord('A') + 1)

    return num


print(excel_col_num())

--- sencond method 

letter = 'FXSHRXW'
n = len(letter)
val = 0
mul = 0

for i in range(n):
  mul =  (26 ** (n-i-1))*(ord(letter[i])-64)
  val += mul

print(val)
