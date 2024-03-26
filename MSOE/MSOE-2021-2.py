def cups_before_refill(capacity, cups):
    water_left = capacity
    cups_made = 0

    for cup in cups:
        water_needed = cup + 1  # Add 1 ounce for the water left in the pod
        water_left -= water_needed
        if water_left < 10:
            print("Filled", cups_made, "cups.")
            return
        cups_made += 1

    print("Filled", cups_made, "cups.")

# Input capacity and cup sizes
capacity = int(input("Enter the capacity of the reservoir: "))
cups = list(map(int, input("Enter the sequence of cup sizes separated by space: ").split()))

# Call the function
cups_before_refill(capacity, cups)
