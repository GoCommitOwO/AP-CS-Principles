import mylibrary
import numpy as np

length = 5
width = 10

arr = np.array([1, 2, 3])
arr2 = np.array([6, 7, 8])


a = mylibrary.area(length, width)
p = mylibrary.perimeter(length, width)

print("Area: ", a)
print("Perimeter: ", p)