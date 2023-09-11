amt_saved = int(input("Amount Saved: "))
interest_rate = float(input("Interest Rate: ")) / 100
times_compounded = int(input("Times Compounded per Year: "))
days = int(input("Number of days: "))

amount = amt_saved * (1 + (interest_rate / times_compounded)) ** (times_compounded * (days / 365))

#output to 2 decimal places
print("The interest earned is: $" + str(round(amount - amt_saved, 2)))
print("The total amount is: $" + str(round(amount, 2)))