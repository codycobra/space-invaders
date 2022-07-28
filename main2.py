
import pygame
# Initialize the pygame
pygame.init()
# screen
screen = pygame.display.set_mode((800, 600))
# Title
pygame.display.set_caption("Long Night of Solace")
icon = pygame.image.load('elite2.png')
pygame.display.set_icon(icon)
# player
playerimg = pygame.image.load('spaceship2.png')
playerx = 370
playery = 480
playerx_change = 0
def player(x, y):
    screen.blit(playerimg, (x, y))
# game loop
running = True
while running:
    screen.fill((19, 0, 26))
    player(playerx, playery)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #handles the key down event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 0.3
            elif event.key == pygame.K_RIGHT:
                playerx_change += 0.3
                #handles the key up event
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    
    playerx += playerx_change
    
    # update screen
    pygame.display.update()

    














































































































