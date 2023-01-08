import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """manage class of ship"""

    def __init__(self, ai_game):
        """initialize the ship and its position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the image of the ship and get the external rectangle
        self.image = pygame.image.load('/Users/tyrionhuu/Codes/Python/python_work/alien_invasion/images/ship.png')
        self.rect = self.image.get_rect()

        # for every new ship, place it in the middle of the screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # save decimal numbers for ship's property
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # sigal of moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """adjust the position according to the signal"""
        # renew the ship instead of adjust position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # renew rect according to self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """draw the ship at the right place"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)