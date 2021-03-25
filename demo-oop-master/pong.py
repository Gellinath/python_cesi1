import pygame
import ball
import paddle
from pygame import draw, display, event, key, Rect
from pygame.constants import K_SPACE, K_s, K_z, K_UP, K_DOWN


pygame.init()

running = True

screen=display.set_mode((800, 600))
(x, y) = (0, 300)
(a, b) = (0, 300)
(k, l) = (794, 250)

r1 = Rect(x-4, y-4,8,8)
r2 = Rect(a,b,6,75)
r3 = Rect(k,l,6,75)

dirrection = "droiteBas"

while running:
    
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    d = 0.05
    d2 = 0.5

    draw.circle(screen, (255, 0, 0), (x, y),  5)
    draw.rect(screen, (255, 0, 0), r1)
    draw.rect(screen, (255, 255, 255), r2)
    draw.rect(screen,(255, 255, 255), r3)

    if (key.get_pressed()[K_z]):
        b-=d2
    if (key.get_pressed()[K_s]):
        b+=d2

    r2 = (a,b,6,75)

    if (key.get_pressed()[K_UP]):
        l-=d2
    if (key.get_pressed()[K_DOWN]):
        l+=d2

    r3 = (k,l,6,75)

    if b<0:
        b=0
    if b>525:
        b=525
    if l<0:
        l=0
    if l>525:
        l=525

    if dirrection == "droite" :
        x +=d
    if dirrection == "droiteBas" :
        x +=d
        y +=d
    if dirrection == "bas" :
        y +=d
    if dirrection == "basGauche" :
        y +=d
        x -=d
    if dirrection == "gauche" :
        x -=d
    if dirrection == "gaucheHaut" :
        x -=d
        y -=d
    if dirrection == "haut" :
        y -=d
    if dirrection == "hautDroite" :
        x +=d
        y -=d

    r1.x = x
    r1.y = y

    if r1.colliderect(r2) == True :
        if y<=7:
            if dirrection == "gaucheHaut" :
                dirrection = "hautDroite"
            elif dirrection == "basGauche" :
                dirrection = "droiteBas"
            elif dirrection == "gauche" :
                dirrection = "droite"

    if r1.colliderect(r3) == True :
        if y>=790:
            if dirrection == "gaucheHaut" :
                dirrection = "hautDroite"
            elif dirrection == "basGauche" :
                dirrection = "droiteBas"
            elif dirrection == "gauche" :
                dirrection = "droite"
    
    if x<0:
        if dirrection == "gaucheHaut" :
            dirrection = "hautDroite"
        elif dirrection == "basGauche" :
            dirrection = "droiteBas"
        elif dirrection == "gauche" :
            dirrection = "droite"
    if x>800:
        if dirrection == "hautDroite" :
            dirrection = "gaucheHaut"
        elif dirrection == "droiteBas" :
            dirrection = "basGauche"
        elif dirrection == "droite" :
            dirrection = "gauche"



    if y<0:
        if dirrection == "hautDroite" :
            dirrection = "droiteBas"
        elif dirrection == "gaucheHaut" :
            dirrection = "basGauche"
    if y>600:
        if dirrection == "droiteBas" :
            dirrection = "hautDroite"
        elif dirrection == "basGauche" :
            dirrection = "gaucheHaut"


    display.update()