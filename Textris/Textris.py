import pygame
import random
import math
import sys
import os
from pygame import mixer

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



pygame.init()
mixer.init()

ended = 0
over = 0

mixer.music.load("sounds\deek.mp3")

leftSound = pygame.mixer.Sound("sounds\Left.wav")
rightSound = pygame.mixer.Sound("sounds\\anti left.wav")
fallDown = pygame.mixer.Sound("sounds\\fall down.wav")
saveChar = pygame.mixer.Sound("sounds\save char.wav")

sansUn = pygame.mixer.Sound("sounds\sans.mp3")
sussSound = pygame.mixer.Sound("sounds\suss.wav")
YEET = pygame.mixer.Sound("sounds\yeet.mp3")
jems = pygame.mixer.Sound("sounds\jems.wav")

goodWord = pygame.mixer.Sound("sounds\good word.wav")
niceWord = pygame.mixer.Sound("sounds\\nice word.wav")
makeWord = pygame.mixer.Sound("sounds\make word stop evil.wav")
makeWord2 = pygame.mixer.Sound("sounds\make word stop good.wav")

story0 = pygame.mixer.Sound("sounds\ANHWUH.wav")

story1 = pygame.mixer.Sound("sounds\GOKMWWBE.wav")
story2 = pygame.mixer.Sound("sounds\HBEKPMMW.wav")

story3 = pygame.mixer.Sound("sounds\JFMWBE.wav")
story4 = pygame.mixer.Sound("sounds\ewqwdt.wav")
end = pygame.mixer.Sound("sounds\FFKPASDS.wav")

comeBack = pygame.mixer.Sound("sounds\come back soon.wav")
dontQuit = pygame.mixer.Sound("sounds\don't quit play more.wav")
fail = pygame.mixer.Sound("sounds\\fail.wav")
mixer.music.set_volume(0.3)
mixer.music.play(-1)


score = 0
points = 0
pad = 0
storedLetter = ""
lastWord = ""
swapped = 0


pygame.display.set_caption('Textris')

# an array with letters distributed in such a way that the more common ones show up more often, that way you won't get 14 Qs in a row.
alpha = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z', 'Z']
#["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","V","V","V","V","V","V","V","V","V","V","V","V","V","V","J","J","J","J","J","J","J","J","J","Z","Z","Z","Z","Z","Z","Z","Z","X","X","X","X","X","Q"]
queue = []
# a dictonary of only 4 letter words to fit with the tetra theme of tetris still. 
words = ["able", "abut", "aced", "aces", "ache", "acid", "acme", "acne", "acre", "acts", "adds", "afar", "aged", "ages", "ahem", "ahoy", "aide", "aids", "ails", "aims", "airs", "ajar", "alas", "ales", "ally", "alma", "aloe", "also", "alto", "amen", "ammo", "anal", "anew", "anon", "ante", "anti", "ants", "apes", "apex", "aqua", "arch", "area", "aria", "arid", "arms", "army", "arts", "arty", "asks", "atom", "atop", "auld", "aunt", "aura", "auto", "avid", "away", "awed", "awol", "awry", "axel", "axis", "axle", "babe", "baby", "back", "bags", "bail", "bait", "bake", "bald", "bale", "balk", "ball", "balm", "band", "bane", "bang", "bank", "barb", "bard", "bare", "barf", "bark", "barn", "bars", "base", "bash", 
"bask", "bass", "bath", "bats", "bawl", "bays", "beak", "beam", "bean", "bear", "beat", "beau", "beck", "beds", "beef", "been", "beep", "beer", "bees", "begs", "bell", "belt", "bend", "bent", "best", "beta", "bets", "bias", "bide", "bids", "bike", "bill", "bind", "bins", "bios", "bird", "bite", "bits", "blab", "blah", "blam", "bled", "blew", "blip", "blob", "bloc", "blot", "blow", "blue", "blur", "boar", "boat", "body", "bogs", "boil", "bold", "bolt", "bomb", "bond", "bone", "bong", "bony", "boob", "book", "boom", "boon", "boot", "bore", "born", "boss", "both", "bout", "bowl", "bows", "boys", "bozo", "brag", "bran", "bras", "brat", "bred", "brew", "brie", "brig", "brim", "bris", "brit", "bros", "brow", "buck", "buds", "buff", "bugs", "bulb", "bulk", "bull", "bump", "bums", "bunk", "buns", "bunt", "burn", "burp", "bury", "bush", "bust", "busy", "buts", "butt", "buys", "buzz", "byes", "cabs", "cafe", "cage", "cake", "calf", "call", "calm", "came", "camp", "cams", "cane", "cans", "cant", "cape", "caps", "carb", "card", "care", "carp", "cars", "cart", "case", "cash", "cast", "cats", "cave", "cell", "cent", "chad", "chap", "chat", "chef", "chew", "chin", "chip", "chop", "chow", "chug", "chum", "cite", "city", "clad", "clam", "clan", "clap", "claw", "clay", "clef", "clip", "clod", "clop", "clot", "club", "clue", "coal", "coat", "coax", "coco", "code", "coed", "coil", "coin", "coke", "cola", 
"cold", "coma", "comb", "come", "comp", "cone", "conk", "cons", "cook", "cool", "coop", "coot", "cope", "cops", "copy", "cord", "core", "cork", "corn", "cost", "cosy", "cots", "coup", "cove", "cows", "cozy", "crab", "cram", "crap", "crew", "crib", "crop", "crow", "crud", "crux", "cube", "cubs", "cued", "cuff", "cult", "cups", "curb", "curd", "cure", "curl", "curt", "cusp", "cuss", "cute", "cuts", "cyst", "dads", "daft", "dais", "dale", "dame", "damn", "damp", "dang", "dare", "dark", "darn", "dart", "dash", "data", "date", "dawn", "days", "daze", "dead", "deaf", "deal", "dean", "dear", "debt", "deck", "deco", "deed", "deem", "deep", "deer", "deft", "defy", "deke", "deli", "dell", "demo", "dent", "deny", "desk", "dewy", "dial", "dibs", "dice", "dick", "died", "dies", "diet", "digs", "dike", "dill", "dime", "dine", "ding", "dink", "dips", "dire", "dirk", "dirt", "disc", "dish", "disk", "ditz", "diva", "dive", "dock", "docs", "doer", "does", "dogs", "dojo", "dole", "doll", "dolt", "dome", "done", "dong", "doom", "door", "dope", "dork", "dorm", "dory", "dose", "dost", "dote", "doth", "dots", "dour", "dove", "down", "doze", "drab", "drag", "draw", "drew", "drip", "drop", "drug", "drum", "dual", "duce", "duck", "duct", "dude", "duds", "duel", "dues", "duet", "duff", "duke", "dull", "duly", "dumb", "dump", "dung", "dunk", "dusk", "dust", "duty", "dyed", "dyer", "each", "earl", "earn", "ears", "ease", "east", "easy", "eats", "echo", "eddy", "edge", "edgy", "edit", "eels", "eggs", 
"egos", "elks", "elms", "else", "emit", "ends", "envy", "epic", "ergo", "eros", "euro", "even", "ever", "eves", "evil", "exam", "exes", "exit", "eyed", "eyes", "eyre", "face", "fact", "fade", "fads", "fail", "fair", "fake", "fall", "fame", "fang", "fans", "fare", "farm", "fart", "fast", "fate", "faun", "faux", "fave", "fear", "feat", "feds", "feed", "feel", "fees", "feet", "fell", "felt", "fend", "fern", "fess", "feta", "feud", "fife", "file", "fill", "film", "find", "fine", "fink", "fins", "fire", "firm", "firs", "fish", "fist", "fits", "five", "fizz", "flag", "flak", "flan", "flap", "flat", "flaw", "flay", "flea", "fled", "flee", "flew", "flex", "flip", "floe", "flog", "flop", "flow", "flue", "flux", "foal", "foam", "foil", "fold", "folk", "fond", "font", "food", "fool", "foot", "ford", "fore", "fork", "form", "fort", "foul", "four", "fowl", "foxy", "frat", "fray", "free", "fret", "frog", "from", "fuel", "fugu", "full", "fund", "funk", "furs", "fury", "fuse", "fuss", "fuzz", "gaff", "gaga", "gage", "gags", "gain", "gala", "gale", "gall", "gals", "game", "gams", "gang", "gaps", "garb", "gasp", "gate", "gave", "gawk", "gays", "gaze", "gear", "geek", "geez", "gels", "gems", "gene", "germ", "gets", "gift", "gigs", "gill", "gimp", "girl", "gist", "give", "glad", "glee", "glen", "glib", "glop", "glow", "glue", "glum", "gnat", "gnaw", "goad", "goal", "goat", "gobs", "gods", "goes", "gold", "golf", "gone", "gong", "good", "goof", "goon", "gore", "gory", "gosh", "gout", "gown", "grab", "grad", "gram", "gran", "gray", "grew", "grey", 
"grid", "grim", "grin", "grip", "grog", "grow", "grub", "guff", "gulf", "gull", "gums", "gunk", "guns", "guru", "gush", "guts", "guys", "gyms", "hack", "hags", "haha", "hail", "hair", "hale", "half", "hall", "halo", "halt", "hams", "hand", "hang", "hank", "haps", "hard", "hare", "harm", "harp", "hash", "hast", "hate", "hath", "hats", "haul", "have", "hawk", "haze", "hazy", "head", "heal", "heap", "hear", "heat", "heck", "heed", "heel", "heft", "heir", "held", "hell", "helm", "help", "hemp", "hens", "herb", "herd", "here", "hero", "hers", "hick", "hide", "high", "hike", "hill", "hilt", "hind", "hint", "hips", "hire", "hiss", "hits", "hive", "hoax", "hobo", "hock", "hoes", "hogs", "hold", "hole", "holt", "holy", "home", "honk", "hood", "hoof", "hook", "hoop", "hoot", "hope", "hops", "horn", "hose", "host", "hots", "hour", "howe", "howl", "hows", "huck", "huge", "hugs", "hula", "hulk", "hull", "hump", "hums", "hung", "hunk", "huns", "hunt", "hurl", "hurt", "hush", "husk", "huts", "hymn", "hype", "hypo", "iced", "icky", "icon", "idea", "idle", "idly", "idol", "iffy", "ills", "inch", "info", "into", "ions", "iris", "iron", "itch", "item", "jabs", "jack", "jade", "jags", "jail", "jake", "jams", "jane", "jars", "java", "jaws", "jazz", "jean", "jeep", "jeez", "jell", "jerk", "jest", "jets", "jews", "jinx", "jobs", "jock", "joey", "join", "joke", "jolt", "josh", "joys", "judo", "jugs", "juke", "jump", "junk", "jury", "just", "kale", "keel", 
"keen", "keep", "kegs", "kelp", "kept", "kern", "keys", "khan", "kick", "kids", "kill", "kiln", "kilo", "kilt", "kind", "king", "kink", "kins", "kiss", "kite", "kiwi", "knee", "knew", "knit", "knob", "knot", "know", "labs", "lace", "lack", "lacy", "lads", "lady", "laid", "lair", "lake", "lamb", "lame", "lamp", "land", "lane", "lang", "laps", "lard", "lark", "lash", "lass", "last", "late", "lava", "lawn", "laws", "lays", "lazy", "lead", "leaf", "leak", "lean", "leap", "lear", "lech", "left", "legs", "lend", "lens", "lent", "less", "lest", "lets", "levy", "lewd", "liar", "lice", "lick", "lido", "lids", "lied", "lien", "lier", "lies", "lieu", "life", "lift", "like", "lily", "limb", "lime", "limo", "limp", "line", "link", "lint", "lion", "lips", "list", "lite", "live", "load", "loaf", "loan", "lobe", "lock", "lode", "loft", "logo", "logs", "loin", "lone", "long", "look", "loom", "loon", "loop", "loos", "loot", "lord", "lore", "lose", "loss", "lost", "lots", "loud", "lout", "love", "lowe", "luau", "lube", "luck", "luge", "lull", "lump", "lung", "lure", "lurk", "lush", "lust", "lutz", "lynx", "mace", "mach", "mack", "made", "mags", "maid", "mail", "maim", "main", "make", "male", "mall", "malt", "mama", "many", "maps", "mare", "mark", "mars", "mart", "mash", "mask", "mass", "mate", "math", "mats", "maul", "maya", "mayo", "maze", "mead", "meal", "mean", "meat", "meet", "melt", "memo", "mend", 
"menu", "meow", "mere", "mesh", "mess", "meta", "mice", "mild", "mile", "milk", "mill", "mime", "mind", "mine", "mini", "mink", "mint", "miss", "mist", "mite", "mitt", "moan", "moat", "mobs", "mock", "mode", "mojo", "mold", "mole", "moms", "monk", "mono", "mood", "moon", "moot", "mope", "mops", "more", "morn", "mort", "moss", "most", "mote", "moth", "move", "much", "muck", "mugs", "mule", "mums", "muse", "mush", "must", "mute", "mutt", "myth", "nada", "nail", "name", "nana", "naps", "narc", "nary", "navy", "near", "neat", "neck", "need", "neon", "nerd", "nest", "news", "newt", "next", "nice", "nick", "nigh", "nine", "node", "nods", "noel", "noir", "none", "noon", "nope", "norm", "nose", "nosh", "nosy", "note", "noun", "nova", "nude", "nuke", "null", "numb", "nuns", "nuts", "oaks", "oars", "oath", "oats", "obey", "oboe", "odds", "odor", "offs", "ogle", "ogre", "oils", "oily", "oink", "okay", "okra", "olds", "omen", "once", "ones", "only", "onto", "oops", "ooze", "opal", "open", "opus", "oral", "orbs", "otto", "ouch", "ours", "outs", "oval", "oven", "over", "owed", "owes", "owls", "owns", "oxen", "pace", "pack", "pact", "pads", "page", "paid", "pail", "pain", "pair", "pale", "palm", "pals", "pane", "pans", "pant", "papa", "pare", "park", "part", "pass", "past", "pate", "path", "pave", "pawn", "paws", "pays", "peak", "pear", "peas", "peat", "peck", "pecs", "peed", "peek", "peel", "peep", 
"peer", "pees", "pelt", "pens", "peon", "perk", "perm", "pest", "pets", "phew", "pick", "pied", "pier", "pies", "pigs", "pike", "pile", "pill", "pimp", "pine", "ping", "pink", "pins", "pint", "pipe", "pits", "pity", "plan", "play", "plea", "pled", "plop", "plot", "plow", "ploy", "plug", "plum", "plus", "pods", "poem", "poet", "poke", "pole", "poll", "polo", "poly", "pond", "pong", "pony", "poof", "pool", "poop", "poor", "pope", "pops", "pore", "pork", "porn", "port", "pose", "post", "pots", "pour", "pout", "pram", "pray", "prep", "prey", "prim", "prod", "prom", "prop", "pros", "puce", "puck", "puff", "puke", "pull", "pulp", "pump", "punk", "puns", "punt", "puny", "pure", "purr", "push", "puss", "puts", "pyre", "quad", "quid", "quit", "quiz", "race", "rack", "racy", "raft", "rage", "rags", "raid", "rail", "rain", "rake", "ramp", "rang", "rank", "rant", "rare", "rash", "rate", "rats", "rave", "rays", "read", "real", "ream", "reap", "rear", "redo", "reds", "reed", "reef", "reek", "reel", "rein", "rely", "rent", "reps", "rest", "ribs", "rice", "rich", "ride", "rife", "riff", "rift", "rigs", "rile", "ring", "rink", "riot", "ripe", "rips", "rise", "risk", "rite", "ritz", "road", "roam", "roar", "robe", "robs", "rock", "rode", "rods", "role", "rolf", "roll", "romp", "roof", "rook", "room", "root", "rope", "rose", "rosy", "rots", "rows", "rube", "rubs", "ruby", "rude", "ruff", "ruin", "rule", "rump", "rune", "rung", "runs", "runt", "ruse", "rush", "rust", "ruth", "sabe", "sack", 
"safe", "saga", "sage", "said", "sail", "sake", "sale", "salt", "same", "sand", "sane", "sang", "sank", "sans", "saps", "sark", "save", "saws", "says", "scab", "scam", "scan", "scar", "scry", "scud", "scum", "seal", "seam", "sear", "seas", "seat", "seed", "seek", "seem", "seen", "seep", "seer", "sees", "self", "sell", "semi", "send", "sent", "sets", "sewn", "sexy", "shag", "sham", "shaw", "shay", "shea", "shed", "shes", "shin", "ship", "shiv", "shoe", "shoo", "shop", "shot", "show", "shun", "shut", "sick", "side", "sift", "sigh", "sign", "silk", "sill", "simp", "sims", "sine", "sing", "sink", "sins", "sire", "sirs", "site", "sits", "size", "skid", "skim", "skin", "skip", "skis", "skit", "slam", "slap", "slaw", "slay", "sled", "slew", "slid", "slim", "slip", "slit", "slob", "slop", "slot", "slow", "slug", "slum", "smog", "smug", "snag", "snap", "snip", "snit", "snob", "snot", "snow", "snub", "snug", "soak", "soap", "soar", "sobs", "sock", "soda", "sofa", "soft", "soil", "sold", "sole", "solo", "some", "song", "sons", "soon", "soot", "sore", "sort", "soul", "soup", "sour", "sown", "span", "spar", "spas", "spat", "spew", "spin", "spit", "spot", "spry", "spud", "spun", "spur", "stab", "stag", "star", "stat", "stay", "stem", "step", "stew", "stir", "stop", "stow", "stub", "stud", "stun", "such", "suck", "suds", "sued", "sues", "suit", "sulk", "sumo", "sump", "sums", "sung", "sunk", "sure", "surf", "suss", "swab", "swam", 
"swan", "swap", "swat", "sway", "swig", "swim", "sync", "tabs", "tack", "taco", "tact", "tags", "tail", "take", "tale", "talk", "tall", "tame", "tank", "tape", "tarp", "tart", "task", "taut", "taxi", "teal", "team", "tear", "teas", "teed", "teen", "tell", "temp", "tend", "tens", "tent", "term", "test", "text", "than", "that", "thaw", "thee", "them", "then", "they", "thin", "this", "thou", "thru", "thug", "thus", "tick", "tide", "tidy", "tied", "tier", "ties", "tiff", "tile", "till", "tilt", "time", "ting", "tins", "tiny", "tips", "tire", "tits", "toad", "tote", "tots", "tour", "town", "toys", "tram", "trap", "tray", "tree", "trek", "trim", "trio", "trip", "trot", "troy", "true", "tuba", "tube", "tubs", "tuck", "tuna", "tune", "turd", "turf", "turk", "turn", "tush", "tusk", "tutu", "twas", "twig", "twin", "twit", "twos", "type", "typo", "tyre", "ugly", "undo", "unit", "unto", "upon", "urge", "urns", "used", "user", "uses", "vain", "vamp", "vary", "vase", "vast", "veal", "veer", "veil", "vein", "vent", "very", "vest", "veto", "vets", "vial", "vibe", "vice", "view", "vile", "vill", "vine", "visa", "void", "volt", "vote", "vows", "wack", "wade", "wage", "waif", "wail", "wait", "wake", "walk", "wall", "wand", "want", "ward", "ware", "warm", "warn", "warp", "wars", 
"wart", "wary", "wash", "wasp", "watt", "wave", "wavy", "waxy", "ways", "weak", "wean", "wear", "webs", "weds", "weed", "week", "weep", "weld", "well", "welt", "went", "wept", "were", "west", "wets", "wham", "what", "whee", "when", "whet", "whew", "whey", "whim", "whip", "whit", "whiz", "whoa", "whom", "whys", "wick", "wide", "wife", "wigs", "wild", "will", "wilt", "wily", "wimp", "wind", "wine", "wing", "wink", "wins", "wipe", "wire", "wise", "wish", "with", "wits", "woes", "woke", "wolf", "womb", "wont", "wood", "woof", "wool", "word", "wore", "work", "worm", "worn", "wrap", "writ", "wuss", "wynn", "yams", "yang", "yank", "yard", "yarn", "yawn", "yeah", "year", "yell", "yeti", "yipe", "yoga", "yogi", "yoke", "yolk", "yore", "your", "yuan", "yuck", "zany", "zeal", "zero", "zest", "zeta", "zing", "zits", "zone", "zoom", "yeet", "aron", "jems", "june", "july", "blog", "tech", "took", 'tool', "told", "asia", "iraq", "ohio", "iowa", "spam", "toll", "utah", "kits", "iran", "unix", "mens", "rome", "dont", "char", "anti", "tone", "wiki", "cuba", "peru", "nike", "tops", "tons", "byte", "isle", "midi", "mega", "nano", "apps", "fiji", "reno", "rugs", "wifi", "guam", "pubs", "lows", "oman", "prix", "maui", "mods", "mali", "laos", "york", "pics" ]

width_of_window = 500
height_of_window = 600


itt = 0
for items in alpha:
    letter = alpha[math.floor((random.random()*100000))%1232]
    queue.append(letter)
curLetter = queue[itt] #alpha[math.floor((random.random()*100000))%1579 ]
nextLetter = queue[itt+1]


window = pygame.display.set_mode((width_of_window,height_of_window))


font = pygame.font.Font('font.ttf', 25)
fontB = pygame.font.Font('font.ttf', 250)

howTo = font.render("HOW TO PLAY:", True, (0, 255, 0))
howToRect = howTo.get_rect()

howTo2 = font.render("MAKE FOUR LETTER WORD", True, (0, 255, 0))
howTo2Rect = howTo2.get_rect()

howTo3 = font.render("LEFT KEY:  LEFT", True, (0, 255, 0))
howTo3Rect = howTo3.get_rect()


howTo4 = font.render("RIGHT KEY: RIGHT", True, (0, 255, 0))
howTo4Rect = howTo4.get_rect()


howTo5 = font.render("DOWN KEY:  FALL", True, (0, 255, 0))
howTo5Rect = howTo5.get_rect()


howTo6 = font.render("UP KEY:    STORE", True, (0, 255, 0))
howTo6Rect = howTo6.get_rect()


howTo7 = font.render("SPACE:     START", True, (0, 255, 0))
howTo7Rect = howTo7.get_rect()

gameOver = font.render("GAME OVER", True, (255, 0, 0))
goRect = gameOver.get_rect()

#story0.play()

howToRect.center = (250,150)
howTo2Rect.center = (250,200)
howTo3Rect.center = (240,250)
howTo4Rect.center = (250,300)
howTo5Rect.center = (240,350)
howTo6Rect.center = (250,400)
howTo7Rect.center = (250,450)
goRect.center = (400, 500)
window.blit(howTo, howToRect)
window.blit(howTo2, howTo2Rect)
window.blit(howTo3, howTo3Rect)
window.blit(howTo4, howTo4Rect)
window.blit(howTo5, howTo5Rect)
window.blit(howTo6, howTo6Rect)
window.blit(howTo7, howTo7Rect)



text = font.render(curLetter, True, (0, 255, 0))
textRect = text.get_rect()

nex = font.render('NEXT:', True, (0, 255, 0))
next = font.render(nextLetter, True, (0, 255, 0))

sco = font.render('SCORE:', True, (0, 255, 0))
scor = font.render(str(points), True, (0+(points/15), 255, 0+(points/15)))

wo = font.render('WORD:', True, (0, 255, 0))
wor = font.render("TEST", True, (0, 255, 0))

sto = font.render('STORE:', True, (0, 255, 0))
stor = font.render("X", True, (0, 255, 0))

nexRect = nex.get_rect()
nextRect = next.get_rect()

scoRect = sco.get_rect()
scorRect = scor.get_rect()

woRect = wo.get_rect()
worRect = wor.get_rect()

stoRect = sto.get_rect()
storRect = stor.get_rect()






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
                                    

def clearUp(loc, Mode):
    if Mode == 1:
        for i in range(loc):
            board[loc-i] = board[(loc-i)-1]
            board[0] = ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]
    if Mode == 2:
        for i in range(20):
            board[i][loc] = '?'
    global score
    score += 1
    if score < 20:
        pygame.time.set_timer(DROP_IT, 500-(score*20))
    else:
        pygame.time.set_timer(DROP_IT, 100)

def drop():
    global over
    if over == 0:
        window.fill((0,0,0))
        for x in range(10):
            for y in range(20):
                rect = pygame.Rect(x * 30, y * 30, 30, 30)
                pygame.draw.rect(window, (255, 255, 255), rect, 1)
                if board[y][x] != '?'  and over == 0:
                    text = font.render(board[y][x], True, (0, 255, 0))
                    rect = pygame.Rect((x * 30) +1, (y * 30)+1, 28, 28)
                    #pygame.draw.rect(window, (255, 100, 0), rect)
                    textRect.center = ((x*30)+15, (y*30)+15)
                    window.blit(text, textRect)     
                    
        pygame.display.update()
        #pygame.draw.rect(window, (255,100,0), [(posX*30)+1, (posY*30)+1, 28, 28], 0)
        textRect.center = ((posX*30)+15, (posY*30)+15)
        nextRect.center = (400, 100)
        nexRect.center = (410,70)
        scoRect.center = (410, 170)
        scorRect.center = (400-pad, 200)
        woRect.center = (400, 270)
        worRect.center = (400,300)
        stoRect.center = (400, 370)
        storRect.center = (400,400)

        text = font.render(curLetter, True, (0, 255, 0))
        next = font.render(nextLetter, True, (0, 255, 0))
        scor = font.render(str(points), True, (0+(points/15), 255, 0+(points/15)))
        stor = font.render(storedLetter, True, (0, 255, 0))
        wor = font.render(lastWord, True, (0, 255, 0))
        window.blit(text, textRect)
        window.blit(next, nextRect)
        window.blit(sco, scoRect)
        window.blit(scor, scorRect)
        window.blit(nex, nexRect)
        window.blit(sto, stoRect)
        window.blit(stor, storRect)
        window.blit(wo, woRect)
        window.blit(wor, worRect)

        for letr in range(10):
            if board[0][letr] != '?':
                window.blit(gameOver, goRect)
                over = 1
                global ended
                if ended == 0:
                    fail.play()
                

        pygame.display.update()  

def scoreIt(curWord):
    egg = 0
    global lastWord
    global ended
    point = 0
    lastWord = curWord
    curWord = curWord.lower()
    for i in curWord:
        global points
        if i == 'e':
            points += 10
            point +=10
        if i == 'a':
            points += 13
            point += 13
        if i == 'i':
            points += 62
            point += 62
        if i == 'l':
            points += 47
            point += 47
        if i == 'n':
            points += 70
            point += 70
        if i == 'o':
            points += 28
            point += 28
        if i == 'r':
            points += 60
            point += 60
        if i == 's':
            points += 19
            point += 19
        if i == 't':
            points += 59
            point += 59
        if i == 'u':
            points += 86
            point += 86
        if i == 'd':
            points += 83
            point += 83
        if i == 'g':
            points += 106
            point += 106
        if i == 'b':
            points += 101
            point += 101
        if i == 'c':
            points += 95
            point += 95
        if i == 'm':
            points += 93
            point += 93
        if i == 'p':
            points += 89
            point += 89
        if i == 'f':
            points += 109
            point += 109
        if i == 'h':
            points += 96
            point += 96
        if i == 'v':
            points += 132
            point += 132
        if i == 'w':
            points += 109
            point += 109
        if i == 'y':
            points += 115
            point += 115
        if i == 'k':
            points += 105
            point += 105
        if i == 'j':
            points += 137
            point += 137
        if i == 'x':
            points += 141
            point += 141
        if i == 'q':
            points += 145
            point += 145
        if i == 'z':
            points += 138
            point += 138
    global pad
    if points > 100 and pad == 0:
        pad+= 20
    if points > 1000 and pad == 20:
        pad+= 25
    if points > 10000 and pad == 40:
        pad+= 25

    if curWord == 'sans' and over == 0:
        sansUn.play()
        egg = 1
    if curWord == 'left' and ended == 0 and over == 0:
        leftSound.play()
        egg = 1
    if curWord == 'suss' and over == 0:
        sussSound.play()
        egg = 1    
    if curWord == 'yeet':
        YEET.play()
        egg = 1 
    if curWord == 'jems' and ended == 0 and over == 0:
        jems.play()
        egg = 1      
    if score == 5 and egg == 0 and over == 0:
        story1.play()
        egg = 1
    if score == 10 and egg == 0 and over == 0:
        story2.play()
        egg = 1
    if score == 15 and egg == 0 and over == 0:
        story3.play()
        egg = 1
    if score == 20 and egg == 0 and over == 0:
        story4.play()
        egg = 1 
    if score == 21 and egg == 0 and over == 0:
        end.play()
        ended = 1
        egg = 1 
    if point < 345 and egg == 0 and ended == 0 and over == 0:
        niceWord.play()
    if point >= 345 and egg == 0 and ended == 0 and over == 0:
        goodWord.play()
    


def checkIt(x, y):
    if x <= 16:
        curWord = board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(y, 2)
                scoreIt(curWord)
                    
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(y, 2)
                scoreIt(reverse(curWord))
    if y < 7:
        curWord = board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
    if y > 0 and y < 8:
        curWord = board[x][y-1] + board[x][y] + board[x][y+1] + board[x][y+2]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
    if y > 1 and y < 9:
        curWord = board[x][y-2] + board[x][y-1] + board[x][y] + board[x][y+1]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
    if y > 2:
        curWord = board[x][y-3] + board[x][y-2] + board[x][y-1] + board[x][y]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
            

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

DROP_IT = pygame.USEREVENT + 1

posX = math.floor((random.random()*1000)%10)
posY = 0
dropped = 0

def left():
    global posX 
    if posX > 0 and dropped == 0:
        posX = posX-1
    # if math.floor((random.random()*1000)%2) == 0:
    #     leftSound.play()

def right():
    global posX 
    if posX <9 and dropped == 0:
        posX = posX + 1
    # if math.floor((random.random()*1000)%2) == 0:
    #     rightSound.play()



def speed():
    global posY, posX, dropped
    if posY > 0:
        for row in range(20):
            if board[row][posX] == '?':
                posY = row
        dropped = 1
    
    
def store():
    global posY, curLetter, nextLetter, itt, swapped, storedLetter, dropped
    dropped = 0
    if storedLetter == "" and swapped == 0 and ended == 0 and over == 0:
        storedLetter = curLetter
        posY = 0
        curLetter = queue[itt+1]
        nextLetter = queue[itt+2]
        itt+=1
        saveChar.play()
        swapped = 1

    if storedLetter != "" and swapped == 0 and ended == 0 and over == 0:
        temp = storedLetter
        storedLetter = curLetter
        posY = 0
        curLetter = temp
        swapped = 1
        saveChar.play()



pygame.display.update()


hostage = math.floor((random.random()*1000)%50)

start = 0

while running:  
    
   
 
 for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
            if event.key == pygame.K_DOWN:
                speed()
            if event.key == pygame.K_UP:
                store()
            if event.key == pygame.K_SPACE and start == 0:
                start = 1
                pygame.time.set_timer(DROP_IT, 500)
            if event.key == pygame.K_ESCAPE:
                quiting = 0
                if hostage > 0:
                    if ended == 0 and quiting == 0:
                        quiting = 1
                        playing = comeBack.play()
                        while playing.get_busy():
                            pygame.time.wait(10) 
                        running = False
                    else:
                        running = False
                if hostage == 0 and ended == 0 and over ==0:
                    dontQuit.play() 
                    hostage+=1
                else:
                    if ended == 0 and quiting == 0:
                        quiting = 1
                        playing = comeBack.play()
                        while playing.get_busy():
                            pygame.time.wait(10) 
                        running = False
                    else:
                        running = False

    if event.type == DROP_IT:
            if over == 0:
                drop()
                if posY <19 and board[posY+1][posX] == '?':
                    posY+=1
                else:
                    board[posY][posX] = curLetter
                    checkIt(posY, posX)
                    posY=0 
                    posX = math.floor((random.random()*1000)%10)
                    text = font.render(curLetter, True, (0, 255, 0))
                    itt += 1
                    curLetter = queue[itt]
                    nextLetter = queue[itt+1]
                    swapped = 0
                    dropped = 0
                
                

                
                

            
    
    if event.type == pygame.QUIT:
        quiting = 0 
        if hostage > 0:
            if ended == 0 and quiting == 0:
                quiting = 1
                playing = comeBack.play()
                while playing.get_busy():
                    pygame.time.wait(10) 
                running = False
            else:
                running = False
        if hostage == 0 and ended == 0 and over ==0:
            dontQuit.play() 
            hostage+=1
        else:
            if ended == 0 and quiting == 0:
                quiting = 1
                playing = comeBack.play()
                while playing.get_busy():
                    pygame.time.wait(10) 
                running = False
            else:
                running = False
            

        


