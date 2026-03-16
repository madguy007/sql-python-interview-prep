# Roman to Integer Conversion

dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}

roman = input()
value = 0

for i in range(len(roman)):
  j = i+1
  if j < len(roman) and dic[roman[i]] < dic[roman[j]]:
    value -= dic[roman[i]]
  else:
    value += dic[roman[i]]

print(value))
