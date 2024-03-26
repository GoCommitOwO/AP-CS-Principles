def generate_triangle_numbers(n):
    triangle_numbers = []
    total = 0
    for i in range(1, n + 1):
        total += i
        triangle_numbers.append(total)
    return triangle_numbers

def split_into_triangle_components(num):
    triangle_nums = generate_triangle_numbers(num)
    components = []
    while num > 0:
        found = False
        for i in reversed(triangle_nums):
            if num >= i:
                components.append(i)
                num -= i
                found = True
                break
        if not found:
            components.append(0)  # append zero if no triangle number found
    return components

def main():
    num = int(input("Enter an integer: "))
    components = split_into_triangle_components(num)
    print("Components as triangle numbers:")
    print(components)

if __name__ == "__main__":
    main()
