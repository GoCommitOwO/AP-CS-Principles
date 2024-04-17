def lengthOfLongestSubstring(s):
    maxLength = 0
    start = 0
    charIndex = {}

    for end in range(len(s)):
        if s[end] in charIndex:
            start = max(start, charIndex[s[end]] + 1)
        charIndex[s[end]] = end
        maxLength = max(maxLength, end - start + 1)

    return maxLength

def main():
    input_str = input("Enter a string: ")
    answer = lengthOfLongestSubstring(input_str)
    print("Length of longest substring without repeating characters:", answer)

if __name__ == "__main__":
    main()
