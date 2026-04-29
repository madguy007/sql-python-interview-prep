def most_occuring_character(input_str):
    # Dictionary to store character frequencies
    char_count = {}

    # Count each character
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    # Find character with highest frequency
    most_occuring_char = max(char_count, key=char_count.get)

    # Return result
    return most_occuring_char, char_count[most_occuring_char]


# Test cases
str1 = "hello"
str2 = "geeksforgeeks"

output1 = most_occuring_character(str1)
output2 = most_occuring_character(str2)

print(f"Input: {str1}, Output: {output1}")
print(f"Input: {str2}, Output: {output2}")