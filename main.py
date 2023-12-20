import pygame
from pygame import freetype
from time import time, sleep

pygame.init()

window = pygame.display.set_mode((500, 500))

keydown = False
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("space pressed!")
            keydown = True
            start = time()
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            print("space up")
            keydown = False
            print("key down for " + start - time())

            
