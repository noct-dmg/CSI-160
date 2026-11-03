import pygame
import sys

from pygame.math import Vector2

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
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.speed = 4
        self.health = 100

        self.image = pygame.Surface((32, 32))
        self.image.fill("cyan")

        self.rect = self.image.get_rect(topleft=(100, 100))

    #movement for WASD and arrows
    def movement_handler(self):
        self.direction = pygame.Vector2(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]: # move up with W and arrow
            self.direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # move down with S and arrow
            self.direction.y += 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # move right with D and arrow
            self.direction.x += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # move left with A and arrow
            self.direction.x -= 1

        if self.direction.length_squared() > 0:
            self.direction.normalize_ip()

        self.rect.move_ip(self.direction * self.speed)
        # lock in screen
        self.rect.clamp_ip(screen.get_rect())

    # For handling sprite updates from other functions.
    def update(self):
        self.movement_handler()

# main game function
def main():
    # Init variables
    noct = Player()
    sprites = pygame.sprite.Group(noct)
    running = True

    # game running in while statement
    while running:
        # Event Handler for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Updating stuff
        sprites.update()

        # fill screen with green for now
        screen.fill((85, 150, 70))


        sprites.draw(screen)
        # Update display
        pygame.display.flip()
        # Tick at FPS for static speed
        clock.tick(FPS)
    # quit game
    pygame.quit()
if __name__ == '__main__':
    main()
