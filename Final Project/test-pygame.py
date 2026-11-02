import pygame
import sys
pygame.init()

# set screen size and also name of screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kokiri Shop Simulator")

# fps cap using clock and tick speed
clock = pygame.time.Clock()

# game variables
player = pygame.Rect(100, 40, 40, 40)
player_speed = 5
# true toggle boolean for loop
running = True




# create loop so pygame runs as screen as long as needed
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               running = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.move_ip(0, 1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pass


    # Repaint screen with green 60 times a second for 60fps
    screen.fill((85, 150, 70))
    #everything after this!!!
    pygame.draw.rect(screen, 'cyan', player)
    # everything before this
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
