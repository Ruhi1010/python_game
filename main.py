import pygame
from settings import Settings
from ship import Ship
from math import floor,ceil
from sys import exit
from bullet import Bullet


class Main:

    def __init__(self):

        #pygame is a wrapper for SDL
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size=(self.settings.width, self.settings.height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()


        #talk about this later
        self.clock = pygame.time.Clock()
        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        while True:
            self.check_events()
            self.render()
            self.ship.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.top <= 50:
                    self.bullets.remove(bullet)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            #flagging
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self.create_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
    
    def create_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            


    def render(self):
        self.screen.fill(self.settings.bg_color) #this is the backaground
        self.render_fps(self.screen, self.clock, self.font)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        

        pygame.display.flip()


        #talk about this later
        self.clock.tick()


    
    #talk about this later
    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner





main = Main()
main.run_game()