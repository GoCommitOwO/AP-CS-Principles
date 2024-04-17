def strong_password_checker(password):
    # Initialize requirements
    has_digit = False
    has_lower = False
    has_upper = False
    
    # Check if password meets requirements
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
    
    # Calculate steps needed to make the password strong
    steps = 0
    if not has_digit:
        steps += 1
    if not has_lower:
        steps += 1
    if not has_upper:
        steps += 1
    
    length = len(password)
    if length < 6:
        steps += max(6 - length, 1)
    elif length > 20:
        steps += length - 20
    
    # Check for consecutive characters
    consecutive = 0
    for i in range(1, length):
        if password[i] == password[i - 1]:
            consecutive += 1
            if consecutive == 2:
                steps += 1
                consecutive = 0
        else:
            consecutive = 0
    
    # Return the maximum of steps needed and length
    return max(steps, 6 - length)

# Test the function
password = "b"
steps_needed = strong_password_checker(password)
print("Steps needed to make the password secure:", steps_needed)
