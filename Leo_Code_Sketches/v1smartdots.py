import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

# Create some random blocks
static_blocks = [[random.randint(20, 780), random.randint(20, 580)] for _ in range(50)]

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -0.5
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 0.5
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -0.5
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 0.5
                lead_x_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(black)
    
    # Draw and update the static blocks
    for block in static_blocks:
        distance = ((block[0]-lead_x)**2 + (block[1]-lead_y)**2)**0.5  # Calculate the distance
        if distance < 50:  # If the block is too close
            if block[0] < lead_x:  # Move the block away
                block[0] -= 1
            else:
                block[0] += 1
            if block[1] < lead_y:
                block[1] -= 1
            else:
                block[1] += 1
        pygame.draw.rect(gameDisplay, red, [block[0], block[1], 10, 10])
    
    pygame.draw.rect(gameDisplay, white, [lead_x,lead_y,10,10])
    pygame.display.update()

    clock.tick(240)

pygame.quit()
quit()
