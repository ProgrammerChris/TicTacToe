import pygame

# TODO: Write win check
# TODO: Display winner and close or restart game


pygame.init()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

# binary representation of players. 0 == X, 1 == O
whos_turn = 0

# Grid
grid =    (
                pygame.Rect(0, 0, 200, 200), pygame.Rect(200, 0, 200, 200), pygame.Rect((400, 0, 200, 200)), # Top row
                pygame.Rect((0, 200, 200, 200)), pygame.Rect(200, 200, 200, 200), pygame.Rect(400, 200, 200, 200), # Middle row
                pygame.Rect(0, 400, 200, 200), pygame.Rect(200, 400, 200, 200), pygame.Rect((400, 400, 200, 200)) # Bottom row
                )

# Keep track of occupied squares
squares_taken = []

# Drawing grid
for square in grid:
    pygame.draw.rect(screen, (255,255,255), square, 1)

# Refresh display
pygame.display.flip()

# Keep display showing until closed.
running = True

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == 6:
            for square in grid:
                if square.collidepoint(event.pos) and square not in squares_taken:
                    if whos_turn == 0:
                        # Draw X
                        pygame.draw.line(screen, (255,255,255), (square[0] + 50, square[1] + 50), (square[0] + 150, square[1] + 150), 15)
                        pygame.draw.line(screen, (255,255,255), (square[0] + 50, square[1] + 150), (square[0] + 150, square[1] + 50), 15)
                    else:
                        # Draw O
                        pygame.draw.circle(screen, (255,255,255), (square[0] + 100, square[1] + 100), 70, 10)
                        
                    squares_taken.append(square)
                    
                    whos_turn = whos_turn ^ 1

                pygame.display.flip()

pygame.quit()

            
