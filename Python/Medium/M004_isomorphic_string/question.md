# Isomorphic Strings

## Problem
Given two strings **s** and **t**, determine if they are **isomorphic**.

Two strings are isomorphic if the characters in **s** can be replaced to get **t**.

Rules:
- All occurrences of a character must map to the same character.
- No two characters may map to the same character.
- A character can map to itself.

## Example 1
Input
egg
add

Output
True

Explanation  
e → a  
g → d

## Example 2
Input
foo
bar

Output
False

Explanation  
The strings cannot be made identical because **'o'** would need to map to both **'a'** and **'r'**.