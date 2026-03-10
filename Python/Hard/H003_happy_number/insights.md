# Insight

This solution uses **two while loops**.

The **outer while loop** repeats the happy number process until the number becomes **1**.

while temp != 1:

Inside this loop, the number is repeatedly replaced by the **sum of the squares of its digits**.

The **inner while loop** is used to calculate the sum of squares of each digit.

while temp:
    digit = temp % 10
    total += digit ** 2
    temp = temp // 10

Steps inside the inner loop:
- Extract the last digit
- Square the digit
- Add it to total
- Remove the last digit

Process flow:

number → break digits → square digits → sum → new number → repeat

If the process eventually **reaches 1**, the number is a **Happy Number**.  
If it keeps repeating in a cycle and never reaches 1, it is **not a Happy Number**.