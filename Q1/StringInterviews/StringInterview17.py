#return the highest frequency character in a string
#they'll only be lowercase vowels

string = input("gimmie yo string\n")

#make an array to store the frequency of each letter
#goes in order of a, e, i, o, u

freq = [0, 0, 0, 0, 0]

if (string.len == 0):
    print("king i need a string LMFAO")
    exit()
elif (string.len == 1):
    print(string)
    exit()

for i in range(0, string.len):
    if (string[i] == 'a'):
        freq[0] += 1
    elif (string[i] == 'e'):
        freq[1] += 1
    elif (string[i] == 'i'):
        freq[2] += 1
    elif (string[i] == 'o'):
        freq[3] += 1
    elif (string[i] == 'u'):
        freq[4] += 1
    else:
        print("king i need a string with only lowercase vowels")
        exit()

#find the highest frequency
highest = 0
for i in range(0, 5):
    if (freq[i] > highest):
        highest = freq[i]

#find the index of the highest frequency
for i in range(0, 5):
    if (freq[i] == highest):
        print ("the most frequent vowel is " + string[i])
        exit()