import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('Jump and Run')
clock = pygame.time.Clock()

colour_surface = pygame.Surface((900,100))
colour_surface.fill('burlywood4')
surface_part2 = pygame.Surface((900,20))
surface_part2.fill('burlywood3')
surface_himmel = pygame.Surface((900,580))
surface_himmel.fill('cornsilk3')
character = pygame.image.load('Bilder/character.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(colour_surface,(0,600))
    screen.blit(surface_part2,(0,500))
    screen.blit(surface_himmel,(0,0))
    screen.blit(character,(200,500))

    pygame.key.get_pressed()

    pygame.display.update()
    clock.tick(60)

