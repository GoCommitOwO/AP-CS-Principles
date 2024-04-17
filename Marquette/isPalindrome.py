input = (input("Enter your word: "))
def isPalindrome(input):
    if input == input[::-1]:
        print("True")
    else:
        print("False")

isPalindrome(input)