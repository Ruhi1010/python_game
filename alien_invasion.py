import sys 

import pygame

from settings import Settings


class Ship:
    def __init__(self, screen):
        ship_image = pygame.image.load('./images/ship_1.png')
        #self.ship_image = pygame.transform.scale(self.ship_image, (40, 50))
        self.ship_image = pygame.transform.scale_by(ship_image, 0.08)
        self.screen = screen
    def blitme(self):
        self.screen.blit(self.ship_image, (570, 670))



class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self.screen)
        
        
        self.clock = pygame.time.Clock()
        
        
        self.font = pygame.font.SysFont("Arial", 24)

        
    # def run_game(self):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
            
    #         self.screen.fill(self.settings.bg_color)
                
    #         pygame.display.flip()
    
    
    def run_game(self):
        x = 50
        y = 50
        while True:
            events = pygame.event.get()
            print(events)
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            self.screen.fill(self.settings.bg_color)
            self.render_fps(self.screen, self.clock, self.font)
            self.ship.blitme()
            
            pygame.draw.rect(self.screen, (0, 255, 0), (x, y, 100, 100))
            x+=.1
            y+=.1
            
            pygame.display.flip()
            
            self.clock.tick()
            
            
    def render_fps(self, screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"FPS: {fps}", True, (255, 100, 100))
        screen.blit(fps_text, (10, 10))
    
# if __name__ == "__main__":
#     ai = AlienInvasion()
#     ai.run_game()



main = AlienInvasion()
main.run_game()