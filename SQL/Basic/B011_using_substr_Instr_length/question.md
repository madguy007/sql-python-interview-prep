You are given a table named Users with the following column:
- Email (varchar): Contains email addresses (e.g., 'john@gmail.com')

Write a SQL query to extract the email provider (domain name without '.com') from each email.

Example:
- 'john@gmail.com' → 'gmail'
- 'alice@yahoo.com' → 'yahoo'

Return the result as a column named Provider.