import pygame
from pygame import freetype
from time import time, sleep

## import os

pygame.init()

window = pygame.display.set_mode((500, 500))

morsecode = {'.-': 'A',
'-...': 'B',
'-.-.': 'C',
'-..': 'D',
'.': 'E',
'..-.': 'F',
'--.': 'G',
'....': 'H',
'..': 'I',
'.---': 'J',
'-.-': 'K',
'.-..': 'L',
'--': 'M',
'-.': 'N',
'---': 'O',
'.--.': 'P',
'--.-': 'Q',
'.-.': 'R',
'...': 'S',
'-': 'T',
'..-': 'U',
'...-': 'V',
'.--': 'W',
'-..-': 'X',
'-.--': 'Y',
'--..': 'Z',
'-----': '0',
'.----': '1',
'..---': '2',
'...--': '3',
'....-': '4',
'.....': '5',
'-....': '6',
'--...': '7',
'---..': '8',
'----.': '9'}

font = freetype.SysFont('Arial', 50)

print(morsecode[".-"])

keydown = False
main = False
while main:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            keydown = True
            start = time()
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            keydown = False
            timedown = time() - start
            ## logic for determining if . or -
            if timedown > 0.2:
                print("-")
            elif timedown < 0.2:
                print(".")

            
