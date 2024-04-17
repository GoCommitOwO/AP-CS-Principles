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

#It is not necessary for you to change the main.
#The main was provided to make sure it conforms
#to the input and output requirenmetns.

def main():
    input_str = input()
    answer = lengthOfLongestSubstring(input_str)
    print(answer)

if __name__ == "__main__":
    main()
