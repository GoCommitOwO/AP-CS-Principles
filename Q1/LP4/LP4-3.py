numeggs = int(input("gimmie yo numba of eggs\n"))

if numeggs < 48:
    priceperegg = 0.50
elif numeggs < 72:
    priceperegg = 0.45
elif numeggs < 132:
    priceperegg = 0.40
else:
    priceperegg = 0.35

totalprice = numeggs * priceperegg

print("yo price per egg is $" + str(priceperegg))
print("yo total price is $" + str(totalprice))