from game_object import GameObject
from pygame import Rect, Surface, Vector2, draw

# Définition de la classe Ball
class Ball(GameObject):

    # Constructeur de la classe
    def __init__(self, pos=Vector2(0, 0)):
        # La position de la balle (Vecteur)
        self.pos = pos
        # La direction de la balle (Vecteur normalisé)
        self.dir = Vector2(1, 1)
        # La vitesse de déplacement de la balle
        self.speed = 0.1
        # Le rayon de la balle en pixel
        self.size = 5

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen
        self.pos = Vector2(screen.get_width()/2, screen.get_height()/2)

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):

        self.pos += self.dir*self.speed

        if self.pos.x >= 800 and self.dir.y == 1:
            self.dir = Vector2(-1,1)
        if self.pos.x >= 800 and self.dir.y == -1:
            self.dir = Vector2(-1,-1)

        if self.pos.x <= 0 and self.dir.y == 1:
            self.dir = Vector2(1,1)
        if self.pos.x <= 0 and self.dir.y == -1:
            self.dir = Vector2(1,-1)

        if self.pos.y >= 600 and self.dir.x == 1:
            self.dir = Vector2(1,-1)
        if self.pos.y >= 600 and self.dir.x == -1:
            self.dir = Vector2(-1,-1)

        if self.pos.y <= 0 and self.dir.x == 1:
            self.dir = Vector2(1,1)
        if self.pos.y <= 0 and self.dir.x == -1:
            self.dir = Vector2(-1,1)

        # Après on la dessine
        draw.circle(self.screen, (255, 255, 255), self.pos, self.size)

    # Renvoi un rectangle aux même dimensions et position que la balle
    def as_rect(self):
        return Rect(self.pos, (self.size, self.size))
