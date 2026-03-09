# Insight

Pascal's Triangle is not like a normal pattern printing problem.  
In many pattern questions we simply use two loops and print values based on `i` and `j`.  
But in Pascal's Triangle the values in each row are not fixed or repetitive, and they depend on the previous row.

The first hint was recognizing that it is still a **triangular pattern**, so two loops are required:

- The **outer loop** iterates through rows.
- The **inner loop** iterates through elements inside each row.

For every row we must create a new empty list to store the elements of that row.

The most important insight was identifying the **if-else condition**:

The **first and last element of every row is always 1**.

This can be detected using the condition:

j == 0 or j == i

Here:
- `j == 0` → first element
- `j == i` → last element of the row

All other elements lie **between these edges**.

For the middle elements, the value depends on the previous row:

triangle[i-1][j-1] + triangle[i-1][j]

So the current element is the **sum of two elements from the previous row**.

This helped me understand that Pascal's Triangle is not just a printing pattern but a pattern that depends on **previous computed values stored in a 2D list**.