import pygame


class Ship:
    def __init__(self, screen):
        ship_image = pygame.image.load('./images/ship_1.png')
        # self.ship_image = pygame.transform.scale(ship_image, (40,200))
        self.ship_image = pygame.transform.scale_by(ship_image, .07)
        self.screen = screen

        self.ship_rect = self.ship_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.ship_rect.y -= 10


        
    def blitme(self):    
        self.screen.blit(self.ship_image, self.ship_rect)