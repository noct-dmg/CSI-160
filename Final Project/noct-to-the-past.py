import pygame
import sys

# init pygame
pygame.init()

# init screen
screen_size = (700,700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Legend of Arhke: Noct to the past")

# set FPS
FPS = 60
clock = pygame.time.Clock()

# Class for player variables
class Player:
    def __init__(self) -> None:
        self.health = 100

    #movement for WASD and arrows
    def movement_handler(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            pass # TODO

# main game function
def main():
    # Init variables
    noct = Player()
    running = True

    # game running in while statement
    while running:
        # Event Handler for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # fill screen with green for now
        screen.fill((85, 150, 70))

        # Update display
        pygame.display.flip()
        # Tick at FPS for static speed
        clock.tick(FPS)
    # quit game
    pygame.quit()
if __name__ == '__main__':
    main()
