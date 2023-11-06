def contains_substring(main_string, sub_string):
    main_len = len(main_string)
    sub_len = len(sub_string)

    for i in range(main_len - sub_len + 1):
        if main_string[i:i + sub_len] == sub_string:
            return True

    return False

# Input two strings
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to check for: ")

if contains_substring(main_string, sub_string):
    print(f"The substring '{sub_string}' is contained within the main string.")
else:
    print(f"The substring '{sub_string}' is not contained within the main string.")
