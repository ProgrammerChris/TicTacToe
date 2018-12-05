#! /usr/bin/env python

import pygame
import os

# TODO: Display winner and close or restart game

pygame.init()

# To reduce CPU Usage! Without this, one core will be used quite heavily
fps = 30
clock = pygame.time.Clock()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_caption('Tic Tac Toe')

# binary representation of players. 0 == X, 1 == O
whos_turn = 0

# Grid
grid =    (
                pygame.Rect(0, 0, 199, 199), pygame.Rect(200, 0, 199, 199), pygame.Rect((400, 0, 199, 199)), # Top row
                pygame.Rect((0, 200, 199, 199)), pygame.Rect(200, 200, 199, 199), pygame.Rect(400, 200, 199, 199), # Middle row
                pygame.Rect(0, 400, 199, 199), pygame.Rect(200, 400, 199, 199), pygame.Rect((400, 400, 199, 199)) # Bottom row
                )

# Current board
board = [
        '_', '_', '_',
        '_', '_', '_',
        '_', '_', '_'
        ]

# Drawing grid
for square in grid:
    pygame.draw.rect(screen, (0, 0, 0), square, 0)

# Updates screen
pygame.display.flip()

# Keep display showing until closed.
running = True

def check_result():
    winner = ''
    global board

    if (    board[3] == board[4] == board[5] != '_' or # Middle row winner
            board[2] == board[4] == board[6] != '_' or # Upwards diagonal winner
            board[1] == board[4] == board[7] != '_' or # Middle column winner
            board[0] == board[4] == board[8] != '_' # Downwards diagonal winner 
        ):

        winner = board[4]

    elif (  board[6] == board[7] == board[8] != '_' or # Bottom winner
            board[2] == board[5] == board[8] != '_' # Right column winner
        ):
        winner = board[8]
    elif (  board[0] == board[1] == board[2] != '_' or # Top row winner
            board[0] == board[3] == board[6] != '_' # Left column winner
        ):
        winner = board[0]

    elif '_' not in board: # If full board but no winners
        winner = 'Draw!'
        
        # TODO: Write text and make 2 buttons inside for exit and restart!

    if winner != '':
        result = '%s wins!'%winner if winner != 'Draw!' else winner
        # Draw ractangle for winner announcement
        pygame.draw.rect(screen, (122, 122, 122), pygame.Rect(150, 250, 300, 100), 0)

        # Font for displaying result
        font_result = pygame.font.SysFont('Arial', 25)

        # Display result in rectangle area
        if result != 'Draw!':
            screen.blit(font_result.render(result, True, (240,240,240)), (260, 260)) # If winner, to center text in rectangle
        else:
            screen.blit(font_result.render(result, True, (240,240,240)), (265, 260)) # If draw, to center text in rectangle
        
        font_buttons = pygame.font.SysFont('Areal', 22)

        # Restart button
        restart_rect = pygame.Rect(180, 300, 100, 40)
        pygame.draw.rect(screen, (125, 255, 125), restart_rect, 0)
        screen.blit(font_buttons.render('Replay', True, (0,0,0)), (205, 312))
        
        # Quit button
        quit_rect = pygame.Rect(320, 300, 100, 40)
        pygame.draw.rect(screen, (255, 125, 125), quit_rect, 0)
        screen.blit(font_buttons.render('Quit', True, (0,0,0)), (355, 312))

        # Button actions
        if restart_rect.collidepoint(event.pos):
            # Re-initialize "board" to keep track of winner or draw
            for i in range(len(board)):
                board[i] = '_'
            global whos_turn
            whos_turn = 0

            # Redraw grid and background
            screen.fill([255, 255, 255])

            for square in grid:
                pygame.draw.rect(screen, (0, 0, 0), square, 0)

            pygame.display.flip()

        elif quit_rect.collidepoint(event.pos):
            global running
            running = False

        pygame.display.update()
        return True
        
while running:
    # CPU Usage control
    clock.tick(fps)
    
    for event in pygame.event.get():

        # Quit if 'X' pressed on window or if 'ESC' is pressed
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        

        # If mouse clicked
        if event.type == pygame.MOUSEBUTTONUP and check_result() != True:
            for square in grid:

                # Check which square is being clicked
                if square.collidepoint(event.pos) and board[grid.index(square)] == '_':
                    if whos_turn == 0:
                        # Draw X in square
                        pygame.draw.line(screen, (255,255,255), (square[0] + 50, square[1] + 50), (square[0] + 150, square[1] + 150), 15)
                        pygame.draw.line(screen, (255,255,255), (square[0] + 50, square[1] + 150), (square[0] + 150, square[1] + 50), 15)
                        board[grid.index(square)] = 'X'
                    else:
                        # Draw O in square
                        pygame.draw.circle(screen, (255,255,255), (square[0] + 100, square[1] + 100), 70, 10)
                        board[grid.index(square)] = 'O'

                    # Clears terminal to show board more nicely in console as it updates. Unix/linux and windows friendly.
                    os.system('cls' if os.name=='nt' else 'clear')

                    # Print board to console. Just because.
                    print(str(board[:3]) + "\n" + str(board[3:6]) + "\n" + str(board[6:9]))

                    pygame.display.update(square)

                    check_result()
                    
                    # Switch turns between X and O
                    whos_turn = whos_turn ^ 1
pygame.quit()
                

    





