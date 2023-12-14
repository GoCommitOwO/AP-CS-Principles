def count_substring_occurrences(source, target):
    count = 0
    start = 0

    while start < len(source):
        index = source.find(target, start)

        if index == -1:
            break

        count += 1
        start = index + 1

    return count

# Get input from the user
source = input("Enter the source string: ")
target = input("Enter the target string: ")

# Count occurrences and display the result
occurrences = count_substring_occurrences(source, target)
print(f'The target "{target}" appears {occurrences} times in the source string.')
