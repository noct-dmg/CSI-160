import pygame
import sys

from pygame.math import Vector2

# init pygame
pygame.init()

# init screen
screen_size = (700,700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Legend of Arhke: Noct to the past")

# set frame and speed settings.
FPS = 60
clock = pygame.time.Clock()

# Class for player variables
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.speed = 180
        self.health = 100

        self.image = pygame.Surface((32, 32))
        self.image.fill("cyan")

        self.rect = self.image.get_rect(topleft=(100, 100))
        self.pos = Vector2(self.rect.topleft)

    #movement for WASD and arrows
    def movement_handler(self, dt):
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

        # Move the floating-point vector first using dt, then update rect
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        # Update rect from precise position
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        # Store position before clamping
        old_pos = self.rect.topleft

        # Keep player inside screen
        self.rect.clamp_ip(screen.get_rect())

        # Only synchronize if clamping actually changed the position
        if self.rect.topleft != old_pos:
            self.pos = Vector2(self.rect.topleft)

    # For handling sprite updates from other functions.
    def update(self, dt):
        self.movement_handler(dt)

# main game function
def main():
    # Init variables
    noct = Player()
    sprites = pygame.sprite.Group(noct)
    running = True
    dt = 0.0

    # game running in while statement
    while running:
        # Event Handler for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Updating stuff
        sprites.update(dt)

        # fill screen with green for now
        screen.fill((85, 150, 70))


        sprites.draw(screen)
        # Update display
        pygame.display.flip()
        # Tick at FPS for static speed
        dt = clock.tick(FPS) / 1000.0
    # quit game
    pygame.quit()
if __name__ == '__main__':
    main()
