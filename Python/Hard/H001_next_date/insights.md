# Insights

## 1. Leap Year Logic
A year is a leap year if:
- Divisible by 400
OR
- Divisible by 4 AND not divisible by 100

Formula:
(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

## 2. Key Idea
Instead of writing multiple if-else blocks for each month,
store month days inside a dictionary.

## 3. Edge Cases
- February in leap year → 29 days
- December 31 → Next year January 1
- End of month → Reset day to 1

## 4. Clean Design Principle
- Avoid duplicate print statements
- Update variables first
- Print once at the end
