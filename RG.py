from specific_rooms import *
a={}
for y in range(len(map)):
    for x in range(len(map)):
        if map[y][x]!=['.']:        
            a[int(str(y)+str(x))]=randint(1,5)
print(a)
