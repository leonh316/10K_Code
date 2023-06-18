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

# Create some random blocks and velocities
static_blocks = [[random.randint(20, 780), random.randint(20, 580)] for _ in range(50)]
block_velocities = [[random.choice([-1, 1]), random.choice([-1, 1])] for _ in range(50)]  # Random initial velocities

score = 0  # Initialize the score

font = pygame.font.Font(None, 36)  # Create a font object

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
    for i, block in enumerate(static_blocks):
        block[0] += block_velocities[i][0]
        block[1] += block_velocities[i][1]
        
        # If the block hits an edge, reverse its velocity
        if block[0] <= 0 or block[0] >= 790:
            block_velocities[i][0] *= -1
        if block[1] <= 0 or block[1] >= 590:
            block_velocities[i][1] *= -1

        pygame.draw.rect(gameDisplay, white, [block[0], block[1], 10, 10])
        
        # Check if the block touches the white dot
        if abs(block[0] - lead_x) < 10 and abs(block[1] - lead_y) < 10:
            score += 1

    # Draw the score
    score_text = font.render(f'Score: {score}', True, white)
    gameDisplay.blit(score_text, (10, 10))

    pygame.draw.rect(gameDisplay, white, [lead_x,lead_y,10,10])
    pygame.display.update()

    clock.tick(240)

pygame.quit()
quit()
