from base_room import *
from random import *

rooms=['g','b','$','c']
current_y,current_x=0,0
def start_room(map):
    global current_y,current_x
    a=[]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x]==['r']:
                b=check_sides(map,y,x,True)
                if len(b)<2:
                    a.append((y,x))
    b=choice(a)
    map[b[0]][b[1]]=['s']
    current_y=b[0]
    current_x=b[1]
    print(current_y,current_x)
start_room(map)


while len(rooms)>0:
    
    a=[]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x]==['r']:
                b=check_sides(map,y,x,True)
                if len(b)>0:
                    a.append((y,x,b))
    room=choice(a)
    side=choice(room[2])
    type_of_room=choice(rooms)
    ar(map,side,type_of_room,room[0],room[1])
    rooms.remove(type_of_room)
for i in map:
    for g in i:
        if g==[]:
            g.append('.')
for i in range (len(map)):
    print(map[i])