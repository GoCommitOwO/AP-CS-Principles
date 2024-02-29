#fill a file called data.dat with 1000 random numbers, two per line
import random
with open("data.dat", "w") as file:
    for i in range(3450):
        file.write(f"{random.randint(100, 500)} {random.randint(100, 500)}\n")
        print('cool im done')