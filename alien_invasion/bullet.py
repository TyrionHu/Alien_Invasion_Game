import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """manage the class of bullet"""
    def __init__(self, ai_game):
        """create a bullet at the ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet at (0, 0), and then set the right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save the position in decimal
        self.y = float(self.rect.y)

    def update(self):
        """moving upward"""
        # renew the position
        self.y -= self.settings.bullet_speed

        # renew rect
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
