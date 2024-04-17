def strongPasswordChecker(s):
    # Initialize requirements
    has_digit = False
    has_lower = False
    has_upper = False

    # Check if password meets requirements
    for char in s:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True

    # Calculate steps needed to make the password strong
    steps = -1
    if not has_digit:
        steps += 1
        s += '1'
    if not has_lower:
        steps += 1
        s += 'a'

    if not has_upper:
        steps += 1
        s += "A"

    length = len(s)

    while length < 6 or length > 20:
        if length < 6:
            steps += 1
            s += 'a'
            length = len(s)
        elif length > 20:
            del s[0]
            length = len(s)


    # Check for consecutive characters
    consecutive = 0
    for i in range(1, length):
        if s[i] == s[i - 1]:
            consecutive += 1
            if consecutive == 2:
                steps += 1
                consecutive = 0
                break
        else:
            consecutive = 0
    return (steps)


def main():
    password = input()
    result = strongPasswordChecker(password)
    print(result)

if __name__ == "__main__":
    main()