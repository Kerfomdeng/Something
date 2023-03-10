
import random
    
map=[[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]]]

room_y=6
room_x=6
additional_chance=None

map[6][6].append('r')
blocked=None
def check_border(room_y,room_x):
    if room_x>=9:
        return 'right'
    elif room_x<=3:
        return 'left'
    if room_y>=9:
        return 'down'
    elif room_y<=3:
        return 'up'
    else:
        return None
def check_sides(map,room_y,room_x,skip_block):
    global blocked
    a=[]
    if skip_block==False:
        b=check_border(room_y,room_x)
    else:
        b=''
    
    try:
        if map[room_y+1][room_x]==[] and blocked !='down' and b!='down':
            if map[room_y+2][room_x]==[]:
                if map[room_y+1][room_x-1]==[]:
                    if map[room_y+1][room_x+1]==[]:
                        a.append('down')
    
    except IndexError:
        pass
    try:
        if map[room_y-1][room_x]==[] and blocked !='up' and b!='up':
            if map[room_y-2][room_x]==[]:
                if map[room_y-1][room_x-1]==[]:
                    if map[room_y-1][room_x+1]==[]:
                        a.append('up')
    except IndexError:
        pass
    try:
        if map[room_y][room_x-1]==[] and blocked !='left' and b!='left':
            if map[room_y][room_x-2]==[]:
                if map[room_y-1][room_x-1]==[]:
                    if map[room_y+1][room_x-1]==[]:
                        a.append('left')
    except IndexError:
        pass
    try:            
        if map[room_y][room_x+1]==[] and blocked !='right' and b!='right': 
            if map[room_y][room_x+2]==[]:
                if map[room_y-1][room_x+1]==[]:
                    if map[room_y+1][room_x+1]==[]:
                        a.append('right')
    except IndexError:
        pass            
    return a
def add_chance(a):
    global additional_chance
    if additional_chance in a:
        a=a*2
        a.remove(additional_chance)
    else:
        pass
    return a

def choise_side(map,room_y,room_x):
    a=add_chance(check_sides(map,room_y,room_x,False))
    try:
        b=random.choice(a)
        return b
    except:
        pass

    
        
def generator(map):
    global blocked
    global room_x
    global room_y
    room_y=6
    room_x=6

    a= choise_side(map,room_y,room_x)
    room_y,room_x=ar(map,a,'r',room_y,room_x)
    for i in range(5):
        z=choise_side(map,room_y,room_x)
        room_y,room_x=ar(map,z,'r',room_y,room_x)
            

            
    return map 

def ar(map,side,room,room_y,room_x):
    global blocked
    global additional_chance
    if side=='down':
        room_y+=1
        map[room_y][room_x].append(room)
        blocked='up'
        additional_chance='down'
    elif side=='up':
        room_y-=1
        map[room_y][room_x].append(room)
        blocked='down'
        additional_chance='up'
    elif side=='left':
        room_x-=1
        map[room_y][room_x].append(room)
        blocked='right'
        additional_chance='left'
    elif side=='right':
        room_x+=1
        map[room_y][room_x].append(room)
        blocked='left'
        additional_chance='right'
    return room_y,room_x
        

generator(map)
generator(map)

