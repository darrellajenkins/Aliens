import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai):
        """Initialze the alien and set its starting position."""
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.image = pygame.image.load('alien.bmp')
        self.music = pygame.mixer.music.load('thrusterFire_000.ogg')  # *** 08/04/24
        pygame.mixer.music.play(-1)  # *** 08/04/24
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
