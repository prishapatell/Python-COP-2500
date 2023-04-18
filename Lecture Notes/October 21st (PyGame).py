# Prisha Patel
# COP 2500 0001
# PyGame
# October 21, 2022
from operator import truediv
import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])

running = True

point = [250,250]
velo =[2,1]
box = [30,30]
bad_box = [450,450]
#                UP   Right  Down   Left     W      A      S      D
key_pressed = [False, False, False, False, False, False, False, False]

red = 0

while( running == True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_LEFT):
                key_pressed[3] = True
            if(event.key == pygame.K_RIGHT):
                key_pressed[1] = True
            if(event.key == pygame.K_UP):
                key_pressed[0] = True
            if(event.key == pygame.K_DOWN):
                key_pressed[2] = True
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_LEFT):
                key_pressed[3] = True
            if(event.key == pygame.K_RIGHT):
                key_pressed[1] = True
            if(event.key == pygame.K_UP):
                key_pressed[0] = True
            if(event.key == pygame.K_DOWN):
                key_pressed[2] = True
# Box Movement
if(key_pressed[0]):
    box[1] -= 1
if(key_pressed[1]):
    box[1] += 1
if(key_pressed[2]):
    box[1] += 1
if(key_pressed[3]):
    box[1] -= 1

# Bad_Box Movement

# Circle Movement
point[0] = point[0] + velo[0]
point[1] += velo[1]
red = (red+1)%256
   
if(point[0] > 500 - 25):
    point[0] = 500 -25
    velo[0] *= -1
if(point[0] < 25):
    point[0] = 25
    velo[0] *= -1

if(point[0] > 475):
    point[0] = 475
    velo[0] *= -1
if(point[0] < 25):
    point[0] = 25
    velo[0] *= -1

# Draw
pygame.draw.circle(screen(red,190,190),(point[0],point[1]),)
pygame.draw.rect(screen,(0,0,255),(box[0]-25,box[1]-25,50,50))