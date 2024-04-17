def count_and_say(n):
    #base case
    if n == 1:
        return "1"

    #initialize previous as "1"
    prev = count_and_say(n-1)
    result = ""
    count = 1 #consecutive digits in a row
    for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i+1]: #increase if curr digit = next digit
                count += 1
            else: #they're different
                result += str(count) + prev[i] #append to result
                count = 1 #reset the count for the next digit
    s = result
    return s

if __name__ == "__main__":
    print("Input an Integer: \n")
    i = int(input())
    print(count_and_say(i))