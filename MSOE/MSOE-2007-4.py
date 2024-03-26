def calculate_distance(address1, address2):
    # Splitting each address into its components
    ns1, ew1 = address1.split()[::2]  # Extracting every second element (distance) starting from index 0
    ns2, ew2 = address2.split()[::2]  # Extracting every second element (distance) starting from index 0

    # Converting directions to factors
    ns_factor = -1 if ns1.endswith('s') else 1
    ew_factor = -1 if ew1.endswith('w') else 1

    # Converting distances to integers
    ns1, ns2, ew1, ew2 = map(int, [ns1[:-1], ns2[:-1], ew1[:-1], ew2[:-1]])

    # Calculating the differences in north-south and east-west distances
    ns_diff = (ns2 - ns1) * ns_factor
    ew_diff = (ew2 - ew1) * ew_factor

    # Calculating the distance using the standard distance formula
    distance = ((ns_diff / 800) ** 2 + (ew_diff / 1200) ** 2) ** 0.5
    return distance

adr1 = input("Enter the first address in the format '100 s 25 e': ")
adr2 = input("Enter the second address in the same format: ")

distance = calculate_distance(adr1, adr2)
print("Distance between the two points:", distance, "miles")
