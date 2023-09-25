#list all the integers from 1 to 20, their squares, square roots, cubes, and fourth roots
#all in a 5 column table

num = 1
print("num\t\tsquare\t\tsqrt\t\tcube\t\tfourth root")
while num <= 20:
    print(str(num) + "\t\t" + str(num**2) + "\t\t" + str(num**0.5) + "\t\t" + str(num**3) + "\t\t" + str(num**0.25))
    num += 1