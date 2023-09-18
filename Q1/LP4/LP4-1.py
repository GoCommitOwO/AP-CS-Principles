numcopies = int(input("gimmie yo numba of copies\n"))

if numcopies < 100:
    pricepercopy = 0.30
elif numcopies < 500:
    pricepercopy = 0.28
elif numcopies < 750:
    pricepercopy = 0.27
elif numcopies < 1000:
    pricepercopy = 0.26
else:
    pricepercopy = 0.25

totalprice = numcopies * pricepercopy

print("yo price per copy is " + str(pricepercopy))
print("yo total price is " + str(totalprice))
