
weight = int(input("gimmie yo weight in kg\n"))
length = int(input("gimmie yo length in cm\n"))
width = int(input("gimmie yo width in cm\n"))
height = int(input("gimmie yo height in cm\n"))

volume = length * width * height

if weight > 27:
    print("your package is too heavy")
    if volume > 100000:
        print(" and too large")
elif volume > 100000:
    print("your package is too large")

else:
    print("your package is good to go")