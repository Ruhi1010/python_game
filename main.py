# # Example file showing a circle moving on screen
# import pygame

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("dark green")

#     pygame.draw.circle(screen, "red", player_pos, 120)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_a]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_d]:
#         player_pos.x += 300 * dt

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     # limits FPS to 60
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     dt = clock.tick(60) / 1000

# pygame.quit()










import pygame
from settings import Settings
from ship import Ship


class Main:

    def __init__(self):

        #pygame is a wrapper for SDL
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size=(
            self.settings.width,
            self.settings.height
        ))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self.screen)
        
        
        #movement flags 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #talk about this later
        self.clock = pygame.time.Clock()
        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        x=100
        y = 100
        while True:
            self.check_events()
            self.render()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            #flagging
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_UP:
                    self.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_UP:
                    self.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False
            
    def render(self):            
        self.screen.fill(self.settings.bg_color) #this is the backaground
        self.render_fps(self.screen, self.clock, self.font)
        self.render_ship()


        self.ship.blitme()


        pygame.display.flip()


            #talk about this later
        self.clock.tick()
    
    
    def render_ship(self):
        if self.moving_right == True:
            self.ship.ship_rect.x += self.settings.ship_speed
        if self.moving_left == True:
            self.ship.ship_rect.x -= self.settings.ship_speed
        if self.moving_up == True:
            self.ship.ship_rect.y -= self.settings.ship_speed
        if self.moving_down == True:
            self.ship.ship_rect.y += self.settings.ship_speed

    
    #talk about this later
    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner





main = Main()
main.run_game()