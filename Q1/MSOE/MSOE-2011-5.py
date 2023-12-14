a6 = -0.09
a5 = 1.6108
a4 = -10.9167
a3 = 34.7625
a2 = -52.0433
a1 = 31.1767
a0 = -4

def fx(x):
    return ((a6 * x**6) + (a5 * x**5) + (a4 * x**4) +
            (a3 * x**3) + (a2 * x**2) + (a1 * x) + a0)

def fpx(x):
    return ((6 * a6 * x**5) + (5 * a5 * x**4) +
            (4 * a4 * x**3) + (3 * a3 * x**2) +
            (2 * a2 * x) + a1)

def newtonsMethod(x):
    #keep going until we're within 0.0001 of the root
    while abs(fx(x)) > 0.0001:
        print("Refined zero: f(" + str(x) + ") = " +
              str(fx(x)))
        x = x - (fx(x) / fpx(x))
    print("Refined zero: f(" + str(x) + ") = " +
          str(fx(x)))
    return x

input = int(input("gimmie yo numba\n"))
newtonsMethod(input)

