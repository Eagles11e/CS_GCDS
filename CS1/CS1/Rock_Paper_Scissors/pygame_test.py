import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

rock = pygame.image.load("rock.png")
rock = pygame.transform.scale(rock, (800,600))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(rock, (0,0))
    pygame.display.flip()
    break
    

screen = pygame.display.set_mode((800, 600))

paper = pygame.image.load("paper.png")
paper = pygame.transform.scale(paper, (800,600))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(paper, (0,0))
    pygame.display.flip()
    time.sleep(2)
    break

screen = pygame.display.set_mode((800, 600))

scissors = pygame.image.load("scissors.png")
scissors = pygame.transform.scale(scissors, (800,600))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(scissors, (0,0))
    pygame.display.flip()
    time.sleep(2)
    break