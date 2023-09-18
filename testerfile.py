import math

b = float(input("side b: "))
c = float(input("side c: "))

if c <= 0 or b <= 0 or c <= b:
# (i can't indent because this is literally a google form, but imagine this next line is indented)
    print("you stupid - that isn't a valid triangle. make sure c < b < 0")
#we've unindented
else:
#indent
    a = math.sqrt((c**2) - (b**2))
    print("the length of side a is: ", str(a))