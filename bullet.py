from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = self.ship.ship_rect.midtop

        self.y = float(self.rect.y)


    def update(self):
        self.y -= 1
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)