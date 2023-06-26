import pygame #Import der Pygame Bibliothek
from sys import exit #Import der Schließung des Spiels

pygame.init()

game_active = True

screen = pygame.display.set_mode((900,700)) #Größe des Displays
pygame.display.set_caption('The Radiant Escape') #Name des Spiels
clock = pygame.time.Clock()

font = pygame.font.Font('Bilder/font.ttf', 50) #Installation der Schriftart

colour_surface = pygame.Surface((900,120)) #Boden im Hintergrund des Spiels
colour_surface.fill('burlywood4')           #Farbe des Bodens
surface_himmel = pygame.Surface((900,580)) #Hintergrund des Spiels
surface_himmel.fill('cornsilk3')            #Farbe des Hintergrundes

def display_score():
    time = int(pygame.time.get_ticks() / 1000)  - start_time #Sekunden, die der Spieler am Leben bleibt
    score_surface = font.render(f'Score: {time}',False,(64,64,64)) #Scoreanzeige während des Spiels
    score_rect = score_surface.get_rect(center = (425,50)) #Formatierung zum Rechteck
    screen.blit(score_surface, score_rect) #Score wird nun auf dem Display angezeigt
    return time

start_time = 3 #Start des Scores

score = 0 #Score zu begin des Spiels

#Endbildschirm
score_end = font.render(f'Game over!',False,(245,177,217)) #Game over wird angezeigt
end_rect = score_end.get_rect(center = (425,250)) #Erstellung eines Rechtecks für die Schrift
end_message = font.render(f'press d for start',False,(245,177,217))
message_rect = end_message.get_rect(center = (425,450))

#Erstellung des characters (Figur, Position)
character = pygame.image.load('Bilder/character.png') #Installation eines Bildes für die Figur
character_rect = character.get_rect(topleft = (200,490)) #Erstellen eines Rechtecks zum besseren Bewegen der Figur
character_gravity = 0 #Erstellung der Schwerkraft-Variable


#Erstellung des Hindernises
hindernis = pygame.image.load('Bilder/hindernis.png') #Installation des Bildes für das Hindernis
hindernis_rect = hindernis.get_rect(topleft = (500,510 ))#Erstellen einses Rechtecks
hindernis_left = 0 #Erstellung der Bewegungs-Variable für das Hindernis



while True:
    for event in pygame.event.get():  #Funktion, um das Spiel beenden zu können
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            

            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE: #bei Tastendruck und anschließendem loslassen um 20 in die Höhe
                character_gravity = -20    
        
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                hindernis_left = -5                                              #bei Tastendruck um 5 nach links
                start_time = int(pygame.time.get_ticks() / 1000)
    
        else:
           if event.type == pygame.KEYDOWN and event.key == pygame.K_d: #Neustart des Spiels
               game_active = True 
               hindernis_rect.left = 900 
               start_time = int(pygame.time.get_ticks() / 1000)


    if game_active:                  
        screen.blit(colour_surface,(0,580)) #Boden wird auf dem Display angezeigt
        screen.blit(surface_himmel,(0,0)) #Himmel wird auf dem Display angezeigt
        screen.blit(hindernis,hindernis_rect) #Hindernis wird auf dem Display angezeigt
        screen.blit(character,character_rect) #Character wird auf dem Display angezeigt

        score = display_score() #Verknüpfung vom Score mit der Anzeige

        #Springbewegung der Figur
        character_gravity += 1 #die Figur fällt
        character_rect.y += character_gravity #Verbindung der Figur mit der Schwerkraft
        hindernis_rect.x += hindernis_left #Verbindung des Hindernises  mit der Bewegung nach links

       

        if character_rect.bottom >= 580: character_rect.bottom = 580 #ein Boden wird erstellt, damit die Figur nicht ins Nichts fällt
        if character_rect.top <= 300: character_rect.top = 450 #Figur springt nicht über den Bildschirmrand hinaus
        if hindernis_rect.left <= -20: hindernis_rect.left = 920 #Hindernis wird immer wieder neu eingesetzt
    

        #Kollision
        if character_rect.colliderect(hindernis_rect): #bei einer Kollison von Figur und Hindernis wird die Variabel game_active zu False
            game_active = False 
    else:
        screen.fill((253,24,62)) #der Bildschirm füllt sich in der vorgegebenen Farbe
        screen.blit(score_end,end_rect) 
        score_final = font.render(f'Score: {score}',False,(245,177,217)) #der erreichte Score wird angezeigt
        final_rect = score_final.get_rect(center = (425,350))    #rstellung eines Rechtecks für den finalen Score 
        screen.blit(score_final,final_rect)
        screen.blit(end_message,message_rect) #eine fianle Nachricht wird angezeigt, die Anweisungen zum Neustart des Spiels gibt
  

    pygame.display.update()
    clock.tick(60)

  