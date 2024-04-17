password = input("Input: ")

num_changes = 0

has_digit = False
has_lowercase = False
has_uppercase = False
correct_length = False
repeats_chars = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.islower():
        has_lowercase = True
    if char.isupper():
        has_uppercase = True

# run the sum
if not has_digit:
    num_changes += 1
if not has_lowercase:
    num_changes += 1
if not has_uppercase:
    num_changes += 1

# consecutive characters check
consecutive = 0
for i in range(1, len(password)):
    if password[i] == password[i-1]:
        consecutive += 1
        if consecutive == 2:
            num_changes +=1
            break
        else:
            consecutive = 0

return num_changes