import pygame
import random
import math 

pygame.init()
screen=pygame.display.set_mode((800,600))
title=pygame.display.set_caption("FISH GAME")
font=pygame.font.Font("freesansbold.ttf", 30)
game_font=pygame.font.Font("freesansbold.ttf",80) 
score=0


#main fish
player_image=pygame.image.load("fish.png")
player_x_position=370
player_y_position=510
player_x_change=0
player_y_change=0

#small fish

small_image=[]
small_x_position=[]
small_y_position=[]
small_x_change=[]
small_y_change=[]
smalls=5

for i in range(smalls):
    small_image.append(pygame.image.load("small_fish.png"))
    small_x_position.append(random.randint(40,725))
    small_y_position.append(random.randint(20,510))
    small_x_change.append(0)
    small_y_change.append(0)


#jellyfish
jelly_image=[]
jelly_x_position=[]
jelly_y_position=[]
jelly_x_change=[]
jelly_y_change=[]
jellys=3

for i in range(jellys):
    jelly_image.append(pygame.image.load("jellyfish.png"))
    jelly_x_position.append(random.randint(50,700))
    jelly_y_position.append(random.randint(50,500))
    jelly_x_change.append(10)
    jelly_y_change.append(10)


def player(x,y):
    screen.blit(player_image,(player_x_position,player_y_position))
    if crash:
        screen.blit(surface,(0,0))
        game_over()


def jelly(x,y,i):
    screen.blit(jelly_image[i],(x,y))


def smallFish(x,y,i):
    screen.blit(small_image[i],(x,y))

def touch(jelly_x_position,jelly_y_position,fish_x_position,fish_y_position,i):
    distance=math.sqrt((math.pow(jelly_y_position-fish_y_position,2))+(math.pow(jelly_x_position-fish_x_position,2)))
    if distance<55:
        return True
    else:
        return False


def scoRe(small_x_position,small_y_position,player_x_position,player_y_position,i):
    distance=math.sqrt((math.pow(small_y_position-player_y_position,2))+(math.pow(small_x_position-player_x_position,2)))
    if distance<43:
        return True
    else :
        return False
def show_score(): 
    score_value=font.render("SCORE: " + str(score),True,(204,0,102)) 
    screen.blit(score_value,(10,10))

def game_over(): 
    game_state=font.render("GAME OVER " ,True,(255,0,0)) 
    screen.blit(game_state,(310,270)) 

running=True
while running:
    screen.fill((255,255,255))
    surface=pygame.image.load("surface.png")
    background=pygame.image.load("ocean.jpg")
    screen.blit(surface,(0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                player_x_change=13
            if event.key==pygame.K_LEFT:
                player_x_change=-13
            if event.key==pygame.K_UP:
                player_y_change=-13
            if event.key==pygame.K_DOWN:
                player_y_change=13
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                player_x_change=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                player_y_change=0

    player_x_position +=player_x_change
    player_y_position += player_y_change
    
    if player_x_position<=0:
        player_x_position=0
    elif player_x_position>685:
        player_x_position=685 

    if player_y_position<=0:
        player_y_position=0
    elif player_y_position>510:
        player_y_position=510 
    
    for i in range(jellys):
        jelly_x_position[i]+=jelly_x_change[i]
        if jelly_x_position[i]<=0:
            jelly_x_change[i]=13
            jelly_y_position[i]+=jelly_y_change[i]
        elif jelly_x_position[i]>685:
            jelly_x_change[i]=-13
            jelly_y_position[i]+=jelly_y_change[i]
    
        if jelly_y_position[i]<=50:
            jelly_y_position[i] += jelly_y_change[i]
        elif jelly_y_position[i]>510:
            jelly_y_position[i]=30
            jelly_y_change[i]-=jelly_y_change[i]
        #game over
        crash=touch(jelly_x_position[i],jelly_y_position[i],player_x_position,player_y_position,i)
        if crash:
            for j in range(jellys):
                jelly_x_change[j]=0
                jelly_y_change[j]=0
                player_x_position=jelly_x_position[j]
                player_y_position=jelly_y_position[j]
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        player_x_change=0
                    elif event.key==pygame.K_LEFT:
                        player_x_change=0
                    if event.key==pygame.K_UP:
                        player_y_change=0
                    elif event.key==pygame.K_DOWN:
                        player_y_change=0
            break

        jelly(jelly_x_position[i],jelly_y_position[i],i)
    for i in range(smalls):
        incerease_score=scoRe(small_x_position[i],small_y_position[i],player_x_position,player_y_position,i)
        if incerease_score:
            small_x_position[i]=random.randint(40,725)
            small_y_position[i]=random.randint(20,510)
            score+=1
            print(score)
        smallFish(small_x_position[i],small_y_position[i],i)

    player(player_x_position,player_y_position)
    show_score()
    
    pygame.display.update()
