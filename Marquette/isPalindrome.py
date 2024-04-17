"""
The function should return a String value saying "True" or "False" the input string is a palindrome or not. See the TODO comments.

Note: The input string contains uppercase and lowercase letters and spaces, but no special characters.

Note: The result should not rely on upper/lowercase letters or spaces.
Ex: "racecar", "RacecAr", and "race car" should all return true.

Input:
@param: string --> String to determine if it is a Palindrome

Output:
A string value.
True: if the input string is a palindrome
False: if the input string is not a palindrome
"""

def isPalindrome(s):
    s = s.strip()
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False

# It is unnecessary to edit the "main" function of each problem's provided code skeleton.
# The main function is written for you in order to help you conform to input and output formatting requirements.

def main():
    input_string = input()
    print(f"{isPalindrome(input_string)}")

main()

