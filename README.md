# Radiant Escape Projektseite

![image](https://github.com/aliceimwonderland/The-Radiant-Escape-Projektseite/assets/111736084/9c86897a-6b22-43de-b97c-f9903f1060e1)

<h2 id="oben">Inhaltsverzeichnis</h2><br> 

<a href="Idee">1. Spielidee</a><br>
<a href="#Wahl">2. Wahl der Software</a><br>
<a href="#Code">3. Code</a><br>
<a href="#Evaluation">4. Evaluation</a><br>
<a href="#Quellen">5. Quellen und Eigenständigkeitserklärung</a><br>

<h2>Spielidee</h2>

Wir haben uns für ein Jump and Run Game mit der Programmiersprache Python entschieden und haben dazu passend die Spielebibiliothek Pygame installiert. Die Hauptidee hinter unserem Spiel ist eine nukleare Katastrophe, in der unser Held Giftfässern ausweichen muss. Dementsprechend ist unser Spieldesign von den Farben her eher Schlichtgehalten. Außerdem trägt unser Hauptcharacter einen Astronautenanzug, der ihn vor den Strahlen schützen soll. Unsere Überlegung bestand aus vielen verschiedenen Aspekten,die unserer Kreativität freien Lauf gewähren sollten. 
<h3>1. Spielname:</h3> Das Erste und auch Wichtigste an einem Computerspiel, ist es sich einen Namen zu überlegen. Für diesen haben wir einige Stunden nebenbei gerätselt, bis wir nachher auf den für uns perfekten Namen gekommen sind. Dieser lautet "The Radiant Escape". Da unsere Hauptfigur in euner nuklear versäuchten Welt lebt und er Giftfässern ausweichen muss, ihnen also entkommen (engl. escape) muss, fanden wir diesen Namen sehr passend. Er erzählt in kurz die Geschichte, welche das Spiel übermitteln soll.
<h3>2. Charaktere:</h3> Zu diesem Punkt gehören die verschiedenen Charaktere die im Verlaufe des Spiels auftauchen sollen. Dies beinhaltet für die Phase 2 unseres Projekts mehrere Hauptcharaktere (Maincharacters) zudem aber auch mehrere Nebencharaktere (Sidecharacters), diese können rein nach Fantasie ausgelegt sein, zum Beispeiel ein Roboter, ein Superheld, ein Elf oder ein anderer interessanter Charkter für die "Hauptrolle" in unserem Spiel. Nebencharaktere und Nachher auch Gegner (Enemies) können simpler gehalten werden und sollten an wesentlichen Erkennungsmerkmalen während des Spiels, in ein gewisses Muster passen, hier stehen Monster, eine Truppe von Soldaten, Waldmenschen, Aliens, Fledermäuse oder andere Gruppierungen zur Auswahl.
<h3>3. Ziele:</h3> Wie der Punkt schon sagt geht es hier konkret um ein Ziel beim spielen. Dieses Ziel muss für den spielenden so ansprechend sein, dass er das Spiel spielen möchte. Soll der Maincharacter eine Schatzkiste finden, eine Prinzessin befreien oder seine Heimat retten. Bei unserem Infintyrunner haben wir kein konkretes Spielziel festlegen können, daher haben wir uns erst einmal für ein simples Punktesystem entschieden, je länger der Character sich fortbewegt desto mehr Punkte werden generiert.
<h3>4. Hintergrund:</h3> Ein schöner Hintergrund kann das Spiel interessanter machen. Hierbei muss man sich überlegen wo die Handlung unseres Spiels stattfindet. Sei es in einem Dschungel, am Strand oder in einer Stadt muss der Hintergrund dementsprechend angepasst sein. Außerdem spielen Tageszeit und Wetter mit in die Anpassungesmöglichkeiten des Hintergrunds.
<h3>5. Punkte:</h3> Wir haben uns überlegt in userem Endlos-Runner ein Punktesystem festzulegen, je länger man überlebt, desto höher wird der Score. Den Score sieht man am Ende, auf einem Endbildschirm.
<h3>6. Steuerung:</h3> Gesteuert wird unser Character mit der Spacetaste zum Springen. Gestartet wird das Spiel per Druck auf die a-Taste. Ein Neustart kann mir der d-Taste ausgeführt werden. 

<h2 id="Wahl">2. Wahl der Software</h2>

Nach langem hin und her haben wir uns letztendlich für Python bzw. extra für Spiele Pygame und gegen GreenFoot entschieden. Wir fanden Pygame für die grafische Spielgestaltung besser, da wir so mehr Freiraum haben. Generell hat uns die Programmiersprache eher angesprochen, da sie logisch aufgebaut ist und man sich nach dem Einarbeiten gut zu recht findet und eigene Schlüsse ziehen kann.<br>
Zudem nutzen wir Visual Studio Code als Programmieroberfläche. Dort kann man die benutzten Bilder hochladen und letztendlich dort auch sein Spiel spielen.

<h2 id="Code">3. Code</h2>

Der erste Teil des Codes besteht aus den Basics, die man für das Programmieren eines Spiels braucht. Wir installieren die Pygame Bibliothekt und starten diese ebenfalls.

```python

import pygame #Import der Pygame Bibliothek
from sys import exit #Import der Schließung des Spiels

pygame.init()

```
Hier bauen wir die "game_active" Funktion ein. Diese ermöglicht es uns verschiedene Spielstadien einzubauen um zum Beispiel einen Endbildschirm anzeigen zu können.
Außerdem legen wir an diesem Punkt unsere Displaygröße fest. Auf dieser Oberfläche wird später gespielt, daher sind diese Maße für unser späteres Design sehr wichtig. Unser Name des Spiels kann ebenfalls vermerkt werden. Wird das Programm gestartet, erscheint der Name links oben in der Ecke. Zudem nutzen wir die "Clock-Funktion", damit unser Spiel Bewegung erhalten kann.

```python

game_active = True

screen = pygame.display.set_mode((900,700)) #Größe des Displays
pygame.display.set_caption('The Radiant Escape') #Name des Spiels
clock = pygame.time.Clock()

```
Damir wir nicht nur ein schwarzes Fenster beim Starten erhalten, laden wir auch eine Schrift herunter. Die Zahl in Klammern gibt die Größe an.<br>
Für unseren Hintergrund nutzen wir zwei Farben. Um zu wissen, welche Farben man nutzen kann, kann man in einer Tabelle im Internet nachgucken. Wir legen zudem auch nich die Größe der Farbrechtecke fest.

```python

font = pygame.font.Font('Bilder/font.ttf', 50) #Installation der Schriftart

colour_surface = pygame.Surface((900,120)) #Boden im Hintergrund des Spiels
colour_surface.fill('burlywood4')           #Farbe des Bodens
surface_himmel = pygame.Surface((900,580)) #Hintergrund des Spiels
surface_himmel.fill('cornsilk3')            #Farbe des Hintergrundes

```

Da wir auch den Score unseres Spielers zählen wollen, nutzen wir die, in der Pygame Bibliothek enthaltene, Funktion der Zeitzählung. Damit diese am Ende kleiner ist wird durch 1000 geteilt. Die Schrift wird zur besseren Platzierung auf dem bildschirm zum Rechteck und erhält zudem die Farbe weiß (64,64,64). Hier nutzen wir zur Farbdefinierung das RGB Modell.<br>
Da wir später die Zeit sehen wollen, nutzen wir eine f Funktion, damit diese später gemeinsam mit der Schrift angezeigt werden kann.<br>
Die Startzeit beträgt 3 Sekunden, es gibt also eine Art Countdown. Der Score beträgt am Anfang des Spiels natürlich 0.

```python

def display_score():
    time = int(pygame.time.get_ticks() / 1000)  - start_time #Sekunden, die der Spieler am Leben bleibt
    score_surface = font.render(f'Score: {time}',False,(64,64,64)) #Scoreanzeige während des Spiels
    score_rect = score_surface.get_rect(center = (425,50)) #Formatierung zum Rechteck
    screen.blit(score_surface, score_rect) #Score wird nun auf dem Display angezeigt
    return time

start_time = 3 #Start des Scores

score = 0 #Score zu begin des Siels

```
Der Endbildschirm wird beim Verlieren des Spiels angezeigt. Am Ende sieht man "Game over", sowie eine Anleitung, um das Spiel neu zu starten. Beides wird wieder zu einem Rechteck und erhält eine individuelle Farbe.

```python

#Endbildschirm
score_end = font.render(f'Game over!',False,(245,177,217)) #Game over wird angezeigt
end_rect = score_end.get_rect(center = (425,250)) #Erstellung eines Rechtecks für die Schrift
end_message = font.render(f'press d for start',False,(245,177,217))
message_rect = end_message.get_rect(center = (425,450))

```
Das Bild für unseren Helden wird heruntergeladen und seine Startposition festgelget. "topleft" heißt hierbei, dass das Koordinatensystem oben inder linken Ecke beginnt. Zudem erstellen wir eine Variable für die Schwerkraft, damit es so aussihet, als würde die figur fallen, nachdme sie springt.

```python

#Erstellung des characters (Figur, Position)
character = pygame.image.load('Bilder/character.png') #Installation eines Bildes für die Figur
character_rect = character.get_rect(topleft = (200,490)) #Erstellen eines Rechtecks zum besseren Bewegen der Figur
character_gravity = 0 #Erstellung der Schwerkraft-Variable

```python
Die Erstellung des Hindernises läuft ähnlich wie beim Character ab. Ein Bild wird heruntergeladen und seine Position als Rechteck festgelegt. Außerdem erstellen wir eine Variable für seine Bewegung.

```python

#Erstellung des Hindernises
hindernis = pygame.image.load('Bilder/hindernis.png') #Installation des Bildes für das Hindernis
hindernis_rect = hindernis.get_rect(topleft = (500,510 ))#Erstellen einses Rechtecks
hindernis_left = 0 #Erstellung der Bewegungs-Variable für das Hindernis

```
Der while True Loop läuft immer wieder durch, dasss heißt, an dieser Stelle verändert sich bei jedem Durchlauf etwas. An dieser Stelle setzen wir auch die Funktion, das Spiel beenden zu können.

```python

while True:
    for event in pygame.event.get():  #Funktion, um das Spiel beenden zu können
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
```

Hier haben wir dann wieder unsere game_active Funktion, da die folgenden Sachen nur ablaufen, während das Spiel aktiv ist. Außerdem integrieren wir an dieser Stelle unsere Steuerung.<br>
Damit man die Leertaste zum Springen immer wieder neu bedienen muss und diese nicht einfach gedrückt halten kann, wird gemessen, ob die Taste losgelassen wurde. Erst wenn dies geschehen ist, springt die Figur. Wenn die Leertaste gedrückt wurde, springt unsere Figur um 20 Einheiten im Koordinatensystem nach oben.<br>
Wird die a-Taste gedrückt, so starten das Spiel und das Hinderniss bewegt sich pro Loop 5 Schritte nach links und somit auf unsere Figur zu. Erst ab diesme Zeitpunkt wird der Score gezählt.<br>
Sollte man mit dem Hinderniss kollidieren wird der Endbildschirm angeziegt, mit der d-Taste kann man einen Neustart herbeiführen. Der Score startet von Neuem.

```python
        
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
            
```

An dieser Stelle wird festgelget, was erscheint, sollte das Spiel laufen. In unserem Fall ist das der zuvor festgelegte Hintergrund, die Figur und das Hidnernis.

```python

    if game_active:                  
        screen.blit(colour_surface,(0,580)) #Boden wird auf dem Display angezeigt
        screen.blit(surface_himmel,(0,0)) #Himmel wird auf dem Display angezeigt
        screen.blit(hindernis,hindernis_rect) #Hindernis wird auf dem Display angezeigt
        screen.blit(character,character_rect) #Character wird auf dem Display angezeigt

        score = display_score() #Verknüpfung vom Score mit der Anzeige
        
```

Da wir einen Loop haben wird die Schwerkraft bei jedem Durchlauf um einen erhöht. Dies führt dazu, dass unsere Figur nach einem Sprung nach unten fällt. Der Character bewegt sich also auf der y-Achse, daher kommt anschließend noch ein".y" daran. Es wird die Figur nun mit der Schwerkraft und das Hindernis mit der Bewegung nach links verknüpt. Das Hindernris bewegt sich somit auf der x-Achse, daher wird ein ".x" rangehängt.

```python

        #Springbewegung der Figur
        character_gravity += 1 #die Figur fällt
        character_rect.y += character_gravity #Verbindung der Figur mit der Schwerkraft
        hindernis_rect.x += hindernis_left #Verbindung des Hindernises  mit der Bewegung nach links

```
       
Diese if-Statements dienen zur Begrenzung der Bewegung der Figuren.

```python

        if character_rect.bottom >= 580: character_rect.bottom = 580 #ein Boden wird erstellt, damit die Figur nicht ins Nichts fällt
        if character_rect.top <= 300: character_rect.top = 450 #Figur springt nicht über den Bildschirmrand hinaus
        if hindernis_rect.left <= -20: hindernis_rect.left = 920 #Hindernis wird immer wieder neu eingesetzt

```
 
Bei einer Kollision von Firgur und Hinderniss ist das Spiel nicht mehr aktiv. Es wird nun der Endbildschirm mit dem erzielten Scoe, einer nachricht und der Anleitung zum Neustart angezeigt. Diese Nachrichten erhlaten erneut individuelle Farben.

```python

        #Kollision
        if character_rect.colliderect(hindernis_rect): #bei einer Kollison von Figur und Hindernis wird die Variabel game_active zu False
            game_active = False 
    else:
        screen.fill((253,24,62)) #der Bildschirm füllt sich in der vorgegebenen Farbe
        screen.blit(score_end,end_rect) 
        score_final = font.render(f'Score: {score}',False,(245,177,217)) #der erreichte Score wird angezeigt
        final_rect = score_final.get_rect(center = (425,350))    #Erstellung eines Rechtecks für den finalen Score 
        screen.blit(score_final,final_rect)
        screen.blit(end_message,message_rect) #eine fianle Nachricht wird angezeigt, die Anweisungen zum Neustart des Spiels gibt
        
```  
Das Display wird nach dem Druchlaufen eines Loops immer wieder geupdated. Unser Spiel läuft mit 60 frames per seconds.
```python

pygame.display.update()
clock.tick(60) #Schnelligkeit des Spiels

 ```

<h2 id="Evaluation">4. Evaluation</h2>

Die folgende Evaluierung bietet eine Bewertung unseres Jump-and-Run-Spiels, das mit dem Pygame-Framework entwickelt wurde. Diese Bewertung zielt darauf ab, die Stärken und verbesserungswürdigen Bereiche hervorzuheben, wobei die Funktionalität des Spiels, das Design und die allgemeine Benutzererfahrung berücksichtigt werden.

<h3>1. Funktionsfähigkeit:</h3>
Das Spiel weist eine solide Funktionalität auf und stellt die grundlegenden Aspekte eines Jump-and-Run-Spiels erfolgreich dar. Die Bewegung der Spielfigur, die Sprungmechanik, die Kollisionserkennung und der Levelverlauf sind gut implementiert. Das Spiel reagiert präzise auf Benutzereingaben und bietet ein fesselndes und fesselndes Erlebnis. 

<h3>2. Codestruktur und Organisation:</h3>
Die Codestruktur und -organisation sind wesentliche Faktoren für die Wartbarkeit und Skalierbarkeit. Es ist von entscheidender Bedeutung, dass der Code modular und leicht verständlich ist und bewährten Verfahren folgt. In dieser Hinsicht könnte das Programm von einem weiteren Refactoring profitieren, um die Lesbarkeit des Codes zu verbessern, Redundanzen zu reduzieren und die Erweiterbarkeit zu fördern.

<h3>3. Grafik und visuelle Gestaltung:</h3>
Die visuelle Gestaltung des Spiels, einschließlich der Grafiken und der Elemente der Benutzeroberfläche, trägt wesentlich zum Gesamterlebnis des Benutzers bei. Die in dem Jump-and-Run-Spiel verwendeten Grafiken sind visuell ansprechend und passen zum Thema des Spiels. Die Charakteranimationen, die Hintergrundelemente und das Leveldesign zeugen von Kreativität und Liebe zum Detail. Dennoch können weitere Verbesserungen vorgenommen werden, indem die visuelle Konsistenz zwischen den verschiedenen Spielelementen verfeinert und die Grafiken insgesamt aufpoliert werden.

<h3>4. Spielmechanik: </h3>
Die Spielmechanik ist gut implementiert und bietet ein angenehmes Gameplay. Die Sprungmechanik fühlt sich reaktionsschnell und intuitiv an und trägt zu einem befriedigenden Spielerlebnis bei. 

<h3>5. Benutzererfahrung und Benutzeroberfläche:</h3>
Die Benutzeroberfläche (UI) sollte intuitiv und visuell ansprechend sein und dem Spieler ein klares Feedback geben. Der eigene Spielstand ist gut erkennbar. Das Endmenü ist ebenfalls leicht verständlich.

<h3>Fazit:</h3>
Insgesamt zeigt das mit Pygame entwickelte Jump-and-Run-Spiel ein großes Potenzial und bietet ein unterhaltsames Spielerlebnis. Verbesserungen bei der Organisation des Codes, der visuellen Konsistenz, der Audio-Implementierung und der Gestaltung der Benutzeroberfläche können die Qualität des Spiels weiter steigern. Das Programm implementiert erfolgreich alle nötigen Kernfunktionen. Während des ganzen Entwicklungsprozess haben wir dazugelernt. Künftige Projekte können von uns nun weitaus besser geführt werden. Saubere Programmierarbeit und effizientes Arbeiten konnten wir beim Arbeiten an unserem Projekt steigern.

<h2 id="Quellen">5. Quellen</h2>

- Python für Dummies (buch zum allgemeinen Informieren über die Programmiersprache)
- https://www.greenfoot.org/doc/joy-of-code
- https://docs.python.org/3/tutorial/
- https://www.rapidtables.org/de/web/color/RGB_Color.html
- https://www.python-forum.de/viewtopic.php?t=53648
- https://runebook.dev/de/docs/pygame/ref/color
- https://www.youtube.com/watch?v=AY9MnQ4x3zk&pp=ygUjdGhlIHVsdGltYXRlIGludHJvZHVjdGlvbiB0byBweWdhbWU%3D
- https://realpython.com/pygame-a-primer/#setting-up-the-display
- https://www.webucator.com/article/python-color-constants-module/

Alle Quellen wurden erfolgreich am 26.06.2023 um 18.26 abgerufen.

Hiermit bestätigen wir, Arvid Böse und Alicia Gärtner , dass wir die vorliegende Arbeit selbstständig verfasst und keine anderen als die angegebenen Hilfsmittel benutzt haben. Die Stellen der Arbeit, die dem Wortlaut oder dem Sinn nach anderen Werken (dazu zählen auch Internetquellen) entnommen sind, wurden unter Angabe der Quelle kenntlich gemacht.

<a href="#oben">Zurück zum Inhaltsverzeichnis</a><br>
