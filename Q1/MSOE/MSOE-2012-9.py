def roman_to_arabic(roman):
    roman_numerals = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    arabic = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]

        if value < prev_value:
            arabic -= value
        else:
            arabic += value

        prev_value = value

    return arabic

# Get input from the user
roman_numeral = input("Enter a Roman numeral: ")

# Convert and display the Arabic (decimal) number
arabic_number = roman_to_arabic(roman_numeral)
print(f'Decimal Value: {arabic_number}')
