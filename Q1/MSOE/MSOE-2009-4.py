import math

# Define the function F(x) based on the provided formula
def F(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)

# Function to approximate the area under the curve using the Riemann sum
def approximate_area(a, b, n):
    h = (b - a) / n
    total_area = 0

    for i in range(n):
        x = a + i * h
        total_area += F(x)

    estimated_area = total_area * h
    return estimated_area

# Get input from the user
a = float(input("Enter the lower bound (a): "))
b = float(input("Enter the upper bound (b): "))
n = int(input("Enter the number of panels (n): "))

# Approximate and display the area under the curve
result = approximate_area(a, b, n)
print(f"Estimated area under the curve: {result}")
