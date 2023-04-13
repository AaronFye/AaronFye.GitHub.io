import pygame
import random
import math

pygame.init()


pygame.display.set_caption('Dude Maker')

colors = ["red","orange","yellow","green","blue","indigo","violet","brown","pink","black","white","teal","mauve","aqua","gray","periwinkle","tan","amber","chartreuse"]
purps = ["blueviolet","darkmagenta","darkorchid","darkorchid1","darkorchid2","darkorchid3","darkorchi4","darkviolet","indigo","magenta","magenta3","mauve",""]
marPurp = [(204, 204, 255),"magenta",(187,133,171), "indigo","violet",(152,115,172)]


width_of_window = 128
height_of_window = 32

running  = True

fps = pygame.time.Clock()

window = pygame.display.set_mode((width_of_window,height_of_window))
window.fill((255,0,255))
DROP_IT = pygame.USEREVENT + 1
#pygame.time.set_timer(DROP_IT, 500)

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


dudes = pygame.image.load('dudesTemp.png')
frontHair = pygame.image.load('frontHair.png')
frontFace = pygame.image.load('frontFace.png')
frontBody = pygame.image.load('frontBody.png')
hand = pygame.image.load('hand.png')
foot = pygame.image.load('foot.png')
liftFoot = pygame.image.load('liftFoot.png')

for i in range(10):

    fill(frontHair, pygame.Color(marPurp[math.floor((random.random()*10000))%6]))
    fill(frontFace, pygame.Color(marPurp[math.floor((random.random()*10000))%6]))
    fill(frontBody, pygame.Color(marPurp[math.floor((random.random()*10000))%6]))
    fill(hand, pygame.Color(marPurp[math.floor((random.random()*10000))%6]))
    footC =pygame.Color(marPurp[math.floor((random.random()*10000))%6])
    fill(foot, footC)
    fill(liftFoot, footC)

    # fill(frontHair, pygame.Color(math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255)))
    # fill(frontFace, pygame.Color(math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255)))
    # fill(frontBody, pygame.Color(math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255)))
    # fill(hand, pygame.Color(math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255), math.floor((random.random()*10000)%255)))
    # footR = math.floor((random.random()*10000)%255)
    # footG = math.floor((random.random()*10000)%255)
    # footB = math.floor((random.random()*10000)%255)
    # fill(foot, pygame.Color("violet"))
    # fill(liftFoot, pygame.Color(footR, footG, footB))

    window.blit(dudes, (0, 0))

    #frontHair build
    window.blit(frontHair, (5, 1))
    window.blit(frontHair, (37, 1))
    window.blit(frontHair, (69, 1))
    window.blit(frontHair, (101, 1))

    #frontFaces build
    window.blit(frontFace, (4, 8))
    window.blit(frontFace, (36, 8))
    window.blit(frontFace, (68, 8))
    window.blit(frontFace, (100, 8))

    #frontBody build
    window.blit(frontBody, (8, 20))
    window.blit(frontBody, (40, 20))
    window.blit(frontBody, (72, 20))
    window.blit(frontBody, (104, 20))

    #hand builder
    window.blit(hand, (4, 22))
    window.blit(hand, (25, 22))

    window.blit(hand, (36, 23))
    window.blit(hand, (57, 21))

    window.blit(hand, (68, 22))
    window.blit(hand, (89, 22))

    window.blit(hand, (68+32, 21))
    window.blit(hand, (89+32, 23))
    #feet builder
    window.blit(foot, (8, 28))
    window.blit(foot, (18, 28))

    window.blit(liftFoot, (8+32, 28))
    window.blit(foot, (18+32, 28))

    window.blit(foot, (8+64, 28))
    window.blit(foot, (18+64, 28))

    window.blit(foot, (8+96, 28))
    window.blit(liftFoot, (18+96, 28))


    pygame.display.update()
    pygame.image.save(window, "purpdudes/image"+str(i)+".png")



while running:  
    
   
 
 for event in pygame.event.get():

    if event.type == DROP_IT:
        a = 0
                

            
    
    if event.type == pygame.QUIT:
        running = False
            

        


