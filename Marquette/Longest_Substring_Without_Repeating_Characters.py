#The function should return the number of characters in the largetst substring
#without a repeating character

#Ex. "abcacbbb -> 3 "abc or "bbb" -> 1 "b

#Input: @param: string -> You enter a string and find the largest subtring

#Output: Integer - The number of characters in the largest substring

def lengthOfLongestSubstring(s):
    maxLength = 0
    #TODO: Fill an array with the characters of the string
    array = ([*s])
    #TODO: Find the longest substring within array
    print(array)
    #Return number of characters within substring

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