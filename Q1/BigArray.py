import random

array = []

for i in range(0, 19):
    array.append(random.randint(20, 90))
    i+= 1

print("Original Array:")
print(array)

#print the array in reverse order
print("\n\nReverse Order:")
for i in range(len(array)-1, -1, -1):
    print(array[i])

#print using a for loop
print("\n\nFor Loop:")
for i in range(0, len(array)):
    print(array[i])

#find the number in the middle
middle_num = array[int(len(array)/2)]
print("\n\nMiddle Number:")
print(middle_num)

#find the average of the first last and middle numbers
average_3 = (array[0] + array[len(array)-1] + middle_num)/3
print("\n\nAverage of first, last, and middle numbers:")
print(average_3)

#find the smallest and largest numbers
smallest = array[0]
largest = array[0]

for i in range(0, len(array)):
    if array[i] < smallest:
        smallest = array[i]
    if array[i] > largest:
        largest = array[i]

print("\n\nSmallest Number:")
print(smallest)
print("Largest Number:")
print(largest)

#switch the largest and smallest numbers

smallest_index = array.index(smallest)
largest_index = array.index(largest)

array[smallest_index] = largest
array[largest_index] = smallest

print("\n\nSwitched Array:")
print(array)

#create a new rand 1-10 and put it in the middle
new_num = random.randint(1, 10)
array[int(len(array)/2)] = new_num

print("\n\nArray With a Random Number 1-10:")
print(array)

#add 10 to every number in the list and print
for i in range(0, len(array)):
    array[i] += 10

print("\n\nArray + 10:")
print(array)

#replace the 3rd number with 5 and print the number removed
removed_num = array[2]
array[2] = 5

print("\n\nRemoved Number:")
print(removed_num)

#numbers in the 50s
print("\n\nNumbers in the 50s:")
for i in range(0, len(array)):
    if array[i] >= 50 and array[i] <= 59:
        print(array[i])

#multiples of 4s
print("\n\nMultiples of 4s:")
for i in range(0, len(array)):
    if array[i] % 4 == 0:
        print(array[i])

#is there a 60 in the list?
print("\n\nIs there a 60 in the list?")
for i in range(0, len(array)):
    if array[i] == 60:
        print("Yes")
        break
    if i == len(array)-1:
        print("No")

#check to see if the list is palindromic
print("\n\nIs the list palindromic?")

palindromic = True
for i in range(0, int(len(array)/2)):
    if array[i] != array[len(array)-1-i]:
        palindromic = False
        break

if palindromic:
    print("Yes")
else:
    print("No")

#how many numbers are greater than the average?
print("\n\nNumbers greater than the average:")

count = 0
average = sum(array)/len(array)

for i in range(0, len(array)):
    if array[i] > average:
        count += 1

print(count)


#how many numbers are even
print("\n\nNumber of Even Elements:")
count = 0

for i in range(0, len(array)):
    if array[i] % 2 == 0:
        count += 1

print(count)

#copy the list into a new list but in reverse
print("\n\nReversed List:")

reversed_list = []

for i in range(len(array)-1, -1, -1):
    reversed_list.append(array[i])

print(reversed_list)

#shift the list to the right by 1, wrapping at the end
print("\n\nShifted List:")

last_num = array[len(array)-1]

for i in range(len(array)-1, 0, -1):
    array[i] = array[i-1]

array[0] = last_num

print(array)

#sum all the digits of the elements
print("\n\nSum of all digits:")
sum_of_digits = 0

for i in range(0, len(array)):
    sum_of_digits += array[i] % 10
    sum_of_digits += array[i] // 10

print(sum_of_digits)