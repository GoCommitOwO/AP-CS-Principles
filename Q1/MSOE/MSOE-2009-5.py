#make program that determines if an input number is prime

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime = int(input("gimmie yo numba\n"))

if isPrime(prime):
    print(str(prime) + " is prime")
else:
    print(str(prime) + " is literally so obviously not prime, are you stupid")