import pygame
from sys import exit 

pygame.init()

game_active = True

screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('Jump and Run')
clock = pygame.time.Clock()

font = pygame.font.Font('Bilder/font.ttf', 50)

colour_surface = pygame.Surface((900,120))
colour_surface.fill('burlywood4')
surface_himmel = pygame.Surface((900,580))
surface_himmel.fill('cornsilk3')

def display_score():
    time = int(pygame.time.get_ticks() / 1000)  - start_time
    score_surface = font.render(f'Score: {time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (425,50))
    screen.blit(score_surface, score_rect)
    
start_time = 0   


#Erstellung des characters (Figur, Position)
character = pygame.image.load('Bilder/character.png') #Installation eines Bildes für die Figur
character_rect = character.get_rect(topleft = (200,490)) #Erstellen eines Rechtecks zum besseren bewegen der Figur
character_gravity = 0 #Ausgangsposition der Figur


#Erstellung der Hindernisse
hindernis = pygame.image.load('Bilder/hinderniss.png') #Installation des Bildes für das Hinderniss
hindernis_rect = hindernis.get_rect(topleft = (500,510 ))#Erstellen einses Rechtecks
hindernis_left = 0




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:         #bei Tastendruck Sprung
                character_gravity = -15  
            elif keys[pygame.K_a]:           #bei Tastendruck nach rechts
                hindernis_left = -5
        
        else:
           if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
               game_active = True 
               hindernis_rect.left = 900 
               start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:                  
        screen.blit(colour_surface,(0,580))
        screen.blit(surface_himmel,(0,0))
        screen.blit(hindernis,hindernis_rect)
        screen.blit(character,character_rect)

        display_score()

        #Springbewegung der Figur
        character_gravity += 1 #die Figur fällt
        character_rect.y += character_gravity #Verbindung der Figur mit der Schwerkraft
        hindernis_rect.x += hindernis_left #Verbindung der Figur mit der Bewegung nach links

        if character_rect.bottom >= 580: character_rect.bottom = 580 #ein Boden wird erstellt, damit die Figur nicht ins Nichts fällt
        if character_rect.top <= 200: character_rect.top = 200 #Figur springt nicht über den Bildschirmrand hinaus
        if hindernis_rect.left <= -20: hindernis_rect.left = 920
    # if character_rect.bottom >= 580: character_rect.bottom 
    
        
        #Kollision
        if character_rect.colliderect(hindernis_rect): 
            game_active = False
    else:
        screen.fill('red')      

    pygame.display.update()
    clock.tick(60)

  