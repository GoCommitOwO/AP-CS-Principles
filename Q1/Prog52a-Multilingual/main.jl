print("donne-moi ton longueur.\n")

len = readline()
len = parse(Int64, len) 

print("donne-moi ton largeur.\n")

wid = readline()
wid = parse(Int64, wid) 

area = len * wid

perim = ((len * 2) + (wid * 2))

print("your area is: ", area, "\n")
print("your perimeter is: ", perim, "\n")