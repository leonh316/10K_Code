import pygame

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
lead_y_change = 0  # Added a y-change variable

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0  # Stop vertical movement when moving horizontally
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0  # Stop vertical movement when moving horizontally
            elif event.key == pygame.K_UP:  # Add control for moving up
                lead_y_change = -10
                lead_x_change = 0  # Stop horizontal movement when moving vertically
            elif event.key == pygame.K_DOWN:  # Add control for moving down
                lead_y_change = 10
                lead_x_change = 0  # Stop horizontal movement when moving vertically

    lead_x += lead_x_change
    lead_y += lead_y_change  # Apply the y-change
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, [lead_x,lead_y,10,10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
