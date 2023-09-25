funnyvarname = int(input("gimmie yo numba\n"))
steps = 0
while True:
    if funnyvarname % 2 == 0:
        print (str(funnyvarname) + " is even, so I take half = " + str(funnyvarname/2))
        funnyvarname = funnyvarname/2
        steps += 1
    elif (funnyvarname % 2 == 1) & (funnyvarname != 1):
        print(str(funnyvarname) + " is odd, so I make 3n + 1 = " + str((funnyvarname*3)+1))
        funnyvarname = (funnyvarname*3)+1
        steps += 1
    elif funnyvarname == 1:
        print("the process took " + str(steps) + " steps to reach 1")
        break



