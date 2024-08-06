import pygame

class GameDemo:
    def __init__(self):
        # init pygame
        pygame.init()
        # create game screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game Demo")
        # set game speed
        self.game_speed = pygame.time.Clock()
        # set background color
        self.bg_color = (255, 255, 255)   # white
    
    def run(self):
        running = True
        center_x = 150
        center_y = 150
        while running:
            # check game events
            for event in pygame.event.get():
                # handle quit event (close window)
                if event.type == pygame.QUIT:
                    running = False
                # handle key down event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        center_x -= 10
                    if event.key == pygame.K_RIGHT:
                        center_x += 10
                    if event.key == pygame.K_UP:
                        center_y -= 10
                    if event.key == pygame.K_DOWN:
                        center_y += 10
            
            # fill background color
            self.screen.fill(self.bg_color)
            # draw a circle
            self.draw_circle(center_x, center_y, radius=100, color=(0, 0, 255))
            # update display
            pygame.display.flip()
            # control game speed
            self.game_speed.tick(30)
        pygame.quit()

    def draw_circle(self, center_x, center_y, radius, color):
        pygame.draw.circle(self.screen, color, (center_x, center_y), radius)


if __name__ == "__main__":
    game = GameDemo()
    game.run()