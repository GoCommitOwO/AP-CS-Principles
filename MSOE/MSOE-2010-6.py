num_points_str = input("Enter the number of points on your polygon: ")
num_points = int(num_points_str.split()[0])

#create an array holding as many user-input
# coordinate pairs as num_points -1, because we reuse the first point as the last one

mondo_array = []
for i in range(num_points):
    string_input = input(f"Enter the x and y coordinates of point #{i}: ")
    #split the string into an array
    split_input = string_input.split()
    x = float(split_input[0])
    y = float(split_input[1])

    #package values into a tuple bc that looks like a coordpair lol
    coord_pair = (x, y)

    mondo_array.append(coord_pair)

area = 0.0

# Calculate the area using surveyor's formula
for i in range(num_points):
    x1, y1 = mondo_array[i]
    x2, y2 = mondo_array[(i + 1) % num_points]
    area += (x1 * y2 - x2 * y1)

area = abs(area) / 2.0

print("The area of the polygon is:", area)
