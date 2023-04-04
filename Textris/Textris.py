import pygame
import random
import math
import time



pygame.init()

pygame.display.set_caption('Textris')


width_of_window = 550
height_of_window = 600

window = pygame.display.set_mode((width_of_window,height_of_window))

running  = True

fps = pygame.time.Clock()



board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] ]


for i in range(20):
    for j in range(10):
        board[i][j] = '?'
                                    



def drop():
    window.fill((0,0,0))
    for x in range(10):
        for y in range(20):
            rect = pygame.Rect(x * 30, y * 30, 30, 30)
            pygame.draw.rect(window, (255, 255, 255), rect, 1)
            if board[y][x] != '?':
                rect = pygame.Rect((x * 30) +1, (y * 30)+1, 28, 28)
                pygame.draw.rect(window, (255, 100, 0), rect)     
                
    pygame.display.update()
    pygame.draw.rect(window, (255,100,0), [(posX*30)+1, (posY*30)+1, 28, 28], 0)
    pygame.display.update()  


DROP_IT = pygame.USEREVENT + 1

pygame.time.set_timer(DROP_IT, 1000)

posX = math.floor((random.random()*1000)%10)
posY = 0

def left():
     global posX 
     if posX > 0:
        posX = posX-1

def right():
     global posX 
     if posX <9:
        posX = posX + 1



pygame.display.update()

while running:  
  
 
 for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(posX)
                left()
            if event.key == pygame.K_RIGHT:
                print(posX)
                right()

    if event.type == DROP_IT:
            drop()
            if posY <19 and board[posY+1][posX] != 'X':
                posY+=1
            else:
                board[posY][posX] = 'X'
                print(board)
                posY=0 
                posX = math.floor((random.random()*1000)%10)

            
    
    if event.type == pygame.QUIT:  
           running = False


