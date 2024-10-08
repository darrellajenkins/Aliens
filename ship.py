import time
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai):  # ai from invasion.py AlienInvasion instance.
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai.screen  # ai instance screen attribute - by way of composition
        self.settings = ai.settings  # ai instance settings attribute - by way of composition
        self.screen_rect = ai.screen.get_rect()  # ai instance screen get_rect attribute - by way of composition
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # forcefield = pygame.mixer.Sound('forceField_003.ogg')  # *** 08/04/24
        # forcefield.play()  # *** 08/04/24
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

