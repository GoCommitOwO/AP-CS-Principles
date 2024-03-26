from sympy.ntheory.factor_ import totient


n = int(input("gimmie yo numba\n"))

totient = totient(n)

print("the totient of " + str(n) + " is " + str(totient))