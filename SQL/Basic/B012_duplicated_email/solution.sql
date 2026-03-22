# Approach 1: Using Dictionary (Optimized)

employees = [
    {"employee_id": 1, "name": "A", "email": "a@gmail.com"},
    {"employee_id": 2, "name": "B", "email": "b@gmail.com"},
    {"employee_id": 3, "name": "C", "email": "a@gmail.com"},
    {"employee_id": 4, "name": "D", "email": "c@gmail.com"},
    {"employee_id": 5, "name": "E", "email": "b@gmail.com"}
]

email_map = {}

# Step 1: Group employees by email
for emp in employees:
    email = emp["email"]
    if email not in email_map:
        email_map[email] = []
    email_map[email].append(emp)

result = []

# Step 2: Filter duplicates and get max employee_id
for email, group in email_map.items():
    if len(group) > 1:
        max_emp = max(group, key=lambda x: x["employee_id"])
        result.append(max_emp)

print(result)


# Approach 2: Using Sorting + One Pass

employees_sorted = sorted(employees, key=lambda x: (x["email"], -x["employee_id"]))

result = []
i = 0
n = len(employees_sorted)

while i < n:
    j = i

    # group same email
    while j < n and employees_sorted[j]["email"] == employees_sorted[i]["email"]:
        j += 1

    # if duplicate group
    if j - i > 1:
        result.append(employees_sorted[i])  # first one has max employee_id

    i = j

print(result)