-- Approach 1: Using SUBSTR + INSTR (Standard SQLite Solution)
SELECT 
    SUBSTR(
        Email,
        INSTR(Email, '@') + 1,
        LENGTH(SUBSTR(Email, INSTR(Email, '@') + 1)) - 4
    ) AS Provider
FROM Users;

-- Approach 2: Cleaner logic using REPLACE
SELECT 
    REPLACE(
        SUBSTR(Email, INSTR(Email, '@') + 1),
        '.com',
        ''
    ) AS Provider
FROM Users;

-- Approach 3: Extract using two INSTR (more flexible)
SELECT 
    SUBSTR(
        Email,
        INSTR(Email, '@') + 1,
        INSTR(SUBSTR(Email, INSTR(Email, '@') + 1), '.') - 1
    ) AS Provider
FROM Users;