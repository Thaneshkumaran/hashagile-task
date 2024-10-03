''Find the First Non-Repeating Character
Write a program to find the first non-repeating character in a string. For input "swiss", the output
should be "w". You cannot use any built-in string or character frequency counting functions.
Instructions: Implement manual string traversal and counting logic to solve the problem.'''
def find_first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
input_str = "swiss"
result = find_first_non_repeating_char(input_str)

if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found.")
