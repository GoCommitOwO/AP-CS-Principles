#IT IS HOT AS HELL IN THIS FUNKY ASS HOT ASS ROOM THAT I'M IN
#IS THAT THE GRIM REAPER?!

t1 = int(input("Time 1: "))
t2 = int(input("Time 2: "))


if (t1 < t2):
    minutes = (t2 - t1) % 100
    hours = (t2 - t1) - minutes
if (t2 < t1):
    minutes = (t1 - t2) % 100
    hours = (t2 - t1) - minutes

print(str(int((hours / 100))) + " hours " + str(minutes) + " minutes.")