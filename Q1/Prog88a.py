#sum difference product average distance maximum

n1 = int(input('gimmie yo first numba, 1-13\n'))
n2 = int(input('gimmie yo second numba, 2-20\n'))

sum = n1 + n2
diff = n1 - n2
prod = n1 * n2
avg = sum / 2
dist = abs(n1 - n2)
if (n1 > n2):
    max = n1
else:
    max = n2

print("original numbas are " + str(n1) + " and " + str(n2))

print ("sum: " + str(sum))
print ("difference: " + str(diff))
print ("product: " + str(prod))
print ("average: " + str(avg))
print ("distance: " + str(dist))
print ("maximum: " + str(max))