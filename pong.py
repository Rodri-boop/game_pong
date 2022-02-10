from ctypes.wintypes import RGB
import sys
import pygame
import random


def ball_animation():
    global ball_speed_x , ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right >=screen_width:
        ball_restar()

    if ball.colliderect(player) or ball.colliderect(oponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom =  screen_height

def oponent_ai():
    if oponent.top < ball.y:
        oponent.top += oponent_speed
    if oponent.bottom > ball.y:
        oponent.bottom -= oponent_speed
    if oponent.top <= 0:
        oponent.top = 0
    if oponent.bottom >= screen_height:
        oponent.bottom =  screen_height

def ball_restar():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


#set up generales
pygame.init()
clock = pygame.time.Clock()

#settings de la ventana principal

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#game rect
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 -70 , 10,140)
oponent = pygame.Rect(10,screen_height/2 -70 ,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
oponent_speed = 7

while True:
    #handling input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        


    ball_animation()
    player_animation()
    oponent_ai()


  
    
    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,oponent)
    pygame.draw.ellipse(screen,RGB(int(random.uniform(1,255)),int(random.uniform(1,255)),int(random.uniform(1,255))),ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(60)#60 == fps
