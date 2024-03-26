def find_longest_repeated(string):
    max_repeat = 0
    longest_repeated_char = ''

    # Find the longest repeated character
    for char in set(string):
        count = string.count(char)
        if count > max_repeat:
            max_repeat = count
            longest_repeated_char = char

    if max_repeat == 1:
        return "No repeated characters found."

    # Traverse the string to find characters repeated max_repeat times
    repeated_chars = []
    for i in range(len(string) - max_repeat + 1):
        if string[i:i + max_repeat] == longest_repeated_char * max_repeat:
            repeated_chars.append(longest_repeated_char)

    return f"{max_repeat} {' '.join(repeated_chars)}"

# Test the function
input_string = input("Enter a string: ")
result = find_longest_repeated(input_string)
print("Longest repeated characters:", result)
