import pygame
from RG import *
class Player:
    def __init__(self, x, y, width, height, texture, speed):
        self.texture=texture
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def update(self):
        self.image =self.texture
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def move(self, direction):
        if direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed
        elif direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed
class Door(pygame.sprite.Sprite):
    def __init__(self,texture,x,y,width,height):
        super().__init__()
        self.size_width = width
        self.size_height =height

        self.image = pygame.transform.scale(pygame.image.load(texture), (width,height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        screen.blit(self.image, (self.rect.x,self.rect.y-15))

# инициализация Pygame
pygame.init()

# создание окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простая игра")

pygame.mixer.init()


pygame.mixer.music.load('TBOI/basement.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()


Music_restart = pygame.USEREVENT + 1
my_event = pygame.event.Event(Music_restart)


# Устанавливаем таймер на 1 секунду, чтобы генерировать наше событие
pygame.time.set_timer(Music_restart, 331000)

Animation = pygame.USEREVENT + 2
my_event = pygame.event.Event(Animation)
pygame.time.set_timer(Animation, 200)

# создание персонажа
player_width = 50
player_height = 50
player_x = 200
player_y = 200
player_speed = 2

img_player_stop=pygame.transform.scale(pygame.image.load("TBOI\\player\\Char.png"), (player_width, player_height))

player = Player(player_x, player_y, player_width, player_height,img_player_stop, player_speed)

room_png= pygame.transform.scale(pygame.image.load('TBOI\\room.png'),(25,25))
current_room_png= pygame.transform.scale(pygame.image.load('TBOI\\current_room.png'),(25,25))
boss_room_png= pygame.transform.scale(pygame.image.load('TBOI\\boss_room.png'),(15,15))
cursed_room_png= pygame.transform.scale(pygame.image.load('TBOI\\cursed_room.png'),(15,15))
gold_room_png= pygame.transform.scale(pygame.image.load('TBOI\\gold_room.png'),(15,15))
shop_png= pygame.transform.scale(pygame.image.load('TBOI\\shop.png'),(15,15))

background=pygame.transform.scale(pygame.image.load('TBOI\\background.png'), (screen_width, screen_height))



#player-up
img_player_up_1=pygame.transform.scale(pygame.image.load("TBOI\\player\\up1.png"), (player_width, player_height))
img_player_up_2=pygame.transform.scale(pygame.image.load("TBOI\\player\\up2.png"), (player_width, player_height))
img_player_up_3=pygame.transform.scale(pygame.image.load("TBOI\\player\\up3.png"), (player_width, player_height))
img_list_player_up=[img_player_up_1,img_player_up_2,img_player_up_3]

#player-down
img_player_down_1=pygame.transform.scale(pygame.image.load("TBOI\\player\\down1.png"), (player_width, player_height))
img_player_down_2=pygame.transform.scale(pygame.image.load("TBOI\\player\\down2.png"), (player_width, player_height))
img_player_down_3=pygame.transform.scale(pygame.image.load("TBOI\\player\\down3.png"), (player_width, player_height))
img_list_player_down=[img_player_down_1,img_player_down_2,img_player_down_3]

#player-left
img_player_left_1=pygame.transform.scale(pygame.image.load("TBOI\\player\\left1.png"), (player_width, player_height))
img_player_left_2=pygame.transform.scale(pygame.image.load("TBOI\\player\\left2.png"), (player_width, player_height))
img_player_left_3=pygame.transform.scale(pygame.image.load("TBOI\\player\\left3.png"), (player_width, player_height))
img_list_player_left=[img_player_left_1,img_player_left_2,img_player_left_3]
#player-right
img_player_right_1=pygame.transform.scale(pygame.image.load("TBOI\\player\\right1.png"), (player_width, player_height))
img_player_right_2=pygame.transform.scale(pygame.image.load("TBOI\\player\\right2.png"), (player_width, player_height))
img_player_right_3=pygame.transform.scale(pygame.image.load("TBOI\\player\\right3.png"), (player_width, player_height))
img_list_player_right=[img_player_right_1,img_player_right_2,img_player_right_3]




def create_map(map,current_y,current_x):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x]!=['.']:
                screen.blit(room_png,(500+25*x,-45+25*y))
                if current_y==y and current_x==x:
                    screen.blit(current_room_png,(500+25*x,-45+25*y))
                if map[y][x]==['b']:
                    screen.blit(boss_room_png,(505+25*x,-40+25*y))
                if map[y][x]==['$']:
                        screen.blit(shop_png,(505+25*x,-40+25*y))
                if map[y][x]==['g']:
                        screen.blit(gold_room_png,(505+25*x,-40+25*y))
                if map[y][x]==['c']:
                        screen.blit(cursed_room_png,(505+25*x,-40+25*y))
def create_doors(map,current_y,current_x):
    global door_down_texture,door_up_texture,door_left_texture,door_right_texture
    a=[]
    if map[current_y-1][current_x]!=['.']:
        if map[current_y-1][current_x]==['r'] or map[current_y-1][current_x]==['s']:
            a.append('Up')
            door_up_texture='TBOI\door_up.png'
        elif map[current_y-1][current_x]==['c']:
            a.append('Up')
            door_up_texture='TBOI\Curse_room_door.png'
        elif map[current_y-1][current_x]==['b']:
            a.append('Up')
            door_up_texture='TBOI\Bossroom.png'
        elif map[current_y-1][current_x]==['g']:
            a.append('Up')
            door_up_texture='TBOI\Golddoor.png'
        elif map[current_y-1][current_x]==['$']:
            a.append('Up')
            door_up_texture='TBOI\Shop_door.png'
    if map[current_y+1][current_x]!=['.']:
        if map[current_y+1][current_x]==['r'] or map[current_y+1][current_x]==['s']:
            a.append('Down')
            door_down_texture='TBOI\door_down.png'
        elif map[current_y+1][current_x]==['c']:
            a.append('Down')
            door_down_texture='TBOI\Curse_room_door_down.png'
        elif map[current_y+1][current_x]==['b']:
            a.append('Down')
            door_down_texture='TBOI\Bossroom_down.png'
        elif map[current_y+1][current_x]==['g']:
            a.append('Down')
            door_down_texture='TBOI\Golddoor_down.png'
        elif map[current_y+1][current_x]==['$']:
            a.append('Down')
            door_down_texture='TBOI\Shop_door_down.png'
    if map[current_y][current_x-1]!=['.']:
        if map[current_y][current_x-1]==['r'] or map[current_y][current_x-1]==['s']:
            a.append('Left')
            door_left_texture='TBOI\door_left.png'
        elif map[current_y][current_x-1]==['c']:
            a.append('Left')
            door_left_texture='TBOI\Curse_room_door_left.png'
        elif map[current_y][current_x-1]==['b']:
            a.append('Left')
            door_left_texture='TBOI\Bossroom_left.png'
        elif map[current_y][current_x-1]==['g']:
            a.append('Left')
            door_left_texture='TBOI\Golddoor_left.png'
        elif map[current_y][current_x-1]==['$']:
            a.append('Left')
            door_left_texture='TBOI\Shop_door_left.png'
    if map[current_y][current_x+1]!=['.']:
        if map[current_y][current_x+1]==['r'] or map[current_y][current_x+1]==['s']:
            a.append('Right')
            door_right_texture='TBOI\door_right.png'
        elif map[current_y][current_x+1]==['c']:
            a.append('Right')
            door_right_texture='TBOI\Curse_room_door_right.png'
        elif map[current_y][current_x+1]==['b']:
            a.append('Right')
            door_right_texture='TBOI\Bossroom_right.png'
        elif map[current_y][current_x+1]==['g']:
            a.append('Right')
            door_right_texture='TBOI\Golddoor_right.png'
        elif map[current_y][current_x+1]==['$']:
            a.append('Right')
            door_right_texture='TBOI\Shop_door_right.png'
        
    return a
            
def check_decor(current_y,current_x):
    if a[int(str(current_y)+str(current_x))]==1:    
        return 1
    elif a[int(str(current_y)+str(current_x))]==2:    
        return 2
    elif a[int(str(current_y)+str(current_x))]==3:    
        return 3
    elif a[int(str(current_y)+str(current_x))]==4:    
        return 4
    elif a[int(str(current_y)+str(current_x))]==5:    
        return 5
                
def object_collide(i):
    global values_up, values_down, values_right, values_left

    if  abs(player.rect.y+20-(i.rect.y+i.size_height))<10 and i.rect.x-player_width< player.rect.x <  (i.rect.x+ i.size_width):
        values_up=False
    #DOWN
    if  abs((player.rect.y+player_height)-i.rect.y)<10 and i.rect.x-player_width< player.rect.x <  (i.rect.x+ i.size_width):
        values_down=False
    #RIGHT
    if  abs((player.rect.x+player_width)-i.rect.x)<10 and i.rect.y-player_height < player.rect.y <  (i.rect.y+ i.size_height)-45:
        values_right=False
    #LEFT
    if  abs(player.rect.x-(i.rect.x+i.size_width))<10 and i.rect.y-player_height < player.rect.y <  (i.rect.y+ i.size_height)-45:
        values_left=False



def room_1():  
    urn1=Door('TBOI\\Urn.png',80,70,60,60)
    urn2=Door('TBOI\\Urn.png',660,70,60,60)
    urn3=Door('TBOI\\Urn.png',80,450,60,60)
    urn4=Door('TBOI\\Urn.png',660,450,60,60)
    rock1=Door('TBOI\\Rock.png',300,200,60,60)
    rock2=Door('TBOI\\Rock.png',430,200,60,60)
    rock3=Door('TBOI\\Rock.png',300,320,60,60)
    rock4=Door('TBOI\\Rock.png',430,320,60,60)
    rock5=Door('TBOI\\Rock.png',370,260,60,60)
    bonfire1=Door('TBOI\\bonfire.png',370,200,60,60)
    bonfire2=Door('TBOI\\bonfire.png',370,320,60,60)
    bonfire3=Door('TBOI\\bonfire.png',300,260,60,60)
    bonfire4=Door('TBOI\\bonfire.png',430,260,60,60)
    list=[urn1,urn2,urn3,urn4,rock1,rock2,rock3,rock4,rock5,bonfire1,bonfire2,bonfire3,bonfire4]
    return list

values_down,values_left,values_right,values_up=True,True,True,True
# основной цикл игры
game_running = True
while game_running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type==Music_restart:
            pygame.mixer.music.play()
        if event.type==Animation:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player.texture=img_list_player_up[0]
                img_list_player_up.pop(0)
                if len(img_list_player_up)==0:
                    img_list_player_up=[img_player_up_1,img_player_up_2,img_player_up_3]
            elif keys[pygame.K_DOWN]:
                player.texture=img_list_player_down[0]
                img_list_player_down.pop(0)
                if len(img_list_player_down)==0:
                    img_list_player_down=[img_player_down_1,img_player_down_2,img_player_down_3]
            elif keys[pygame.K_RIGHT]:
                player.texture=img_list_player_right[0]
                img_list_player_right.pop(0)
                if len(img_list_player_right)==0:
                    img_list_player_right=[img_player_right_1,img_player_right_2,img_player_right_3]
            elif keys[pygame.K_LEFT]:
                player.texture=img_list_player_left[0]
                img_list_player_left.pop(0)
                if len(img_list_player_left)==0:
                    img_list_player_left=[img_player_left_1,img_player_left_2,img_player_left_3]
            else:
                player.texture=img_player_stop

    # обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.rect.top > 30 and values_up!=False:
        player.move("up")
    elif keys[pygame.K_DOWN] and player.rect.bottom < screen_height-30 and values_down!=False:
        player.move("down")
    if keys[pygame.K_LEFT] and player.rect.left > 30 and values_left!=False:
        player.move("left")
    if keys[pygame.K_RIGHT] and player.rect.right < screen_width-30 and values_right!=False:
        player.move("right")
    values_up=True
    values_down=True
    values_left=True
    values_right=True

    # отрисовка экрана
    screen.blit(background,(0, 0))
    player.update()
    if check_decor(current_y,current_x)==1:
        
        for i in room_1() :
            i.update()
            object_collide(i)
    create_map(map,current_y,current_x)    
    if 'Up' in create_doors(map,current_y,current_x):
        door_up=Door(door_up_texture,350,40,100,75)
        door_up.update()
        if pygame.sprite.collide_rect(door_up, player):
            current_y-=1
            player.rect.y=450
    else:
        try:
            del door_up
        except:
            pass
    if 'Down' in create_doors(map,current_y,current_x):
        door_down=Door(door_down_texture,350,515,100,75)
        door_down.update()
        if pygame.sprite.collide_rect(door_down, player):
            current_y+=1
            player.rect.y=115
    else:
        try:
            del door_down
        except:
            pass
    if 'Left' in create_doors(map,current_y,current_x):
        door_left=Door(door_left_texture,22,265,65,100)
        door_left.update()
        if pygame.sprite.collide_rect(door_left, player):
            current_x-=1
            player.rect.x=600
    else:
        try:
            del door_left
        except:
            pass
    if 'Right' in create_doors(map,current_y,current_x):
        door_right=Door(door_right_texture,705,265,65,100)
        door_right.update()
        if pygame.sprite.collide_rect(door_right, player):
            current_x+=1
            player.rect.x=100
    else:
        try:
            del door_right
        except:
            pass

            
    
    pygame.display.update()

# завершение работы Pygame
pygame.quit()
