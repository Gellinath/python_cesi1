from pygame import key, Rect, Surface, Vector2, draw, Rect
from pygame.constants import K_DOWN, K_UP, K_z, K_s
from game_object import GameObject
from objects.ball import Ball

# Définition de la classe Paddle
class Paddle(GameObject):

    # Constructeur de la classe
    def __init__(self, ball: Ball = None, is_player=True):
        # Position de la raquette
        self.pos = Vector2(5, 300)
        # Taille de la raquette
        self.size = Vector2(5, 100)
        # La raquette est controlée par le joueur ? O/N
        self.is_player = is_player
        # Quelle est la balle du jeu (pour l'IA)
        self.ball = ball
        # Vitesse de déplacement de la raquette
        self.speed = 0.5

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):
        # Il existe une fonction par type de joueur, manuel ou IA
        if (self.is_player):
            self.manual_control()
        else:
            self.automatic_control()

        # Maintenant que les coordonées ont changés, on dessine la raquette
        draw.rect(self.screen, (255, 255, 255), self.as_rect())

    def manual_control(self):
        # Ici vous mettez votre logique de mouvement, avec les touches de clavier etc.
        if (key.get_pressed()[K_UP]):
            self.pos.y -= self.speed
        if (key.get_pressed()[K_DOWN]):
            self.pos.y += self.speed
        if self.pos.y >= 500:
            self.pos.y = 500
        if self.pos.y <= 0:
            self.pos.y = 0
        return

    # Imbattable, la raquette suis la balle directement sans faute
    def automatic_control(self):
        self.pos.y = self.ball.pos.y - 50
        self.pos.x = 790
        if self.pos.y >= 500:
            self.pos.y = 500
        if self.pos.y <= 0:
            self.pos.y = 0
        return

    # On se sert de la position et de la taille pour construire un rectangle
    def as_rect(self):
        return Rect(self.pos, self.size)