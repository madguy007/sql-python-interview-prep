year = int(input())
month = int(input())
day = int(input())

# Leap year check
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Days in each month
m_days = {
    1: 31,
    2: 29 if is_leap else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Check end of month
if day == m_days[month]:
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    day = 1
else:
    day += 1

print(f"The next date is [yyyy-mm-dd] {year:04d}-{month:02d}-{day:02d}")
