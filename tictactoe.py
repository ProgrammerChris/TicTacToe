#! /usr/bin/env python

import pygame
import os

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

# Current board
board = [
        '_', '_', '_',
        '_', '_', '_',
        '_', '_', '_'
        ]

# Drawing grid
for square in grid:
    pygame.draw.rect(screen, (255,255,255), square, 1)

# Updates screen
pygame.display.flip()

# Keep display showing until closed.
running = True

def check_result():
    winner = ''

    if (    board[3] == board[4] == board[5] != '_' or # Middle row winner
            board[2] == board[4] == board[6] != '_' or # Upwards diagonal winner
            board[1] == board[4] == board[7] != '_' or # Middle column winner
            board[0] == board[4] == board[8] != '_' # Downwards diagonal winner 
        ):

        winner = board[4]
        print('Winner', winner)
        return winner

    elif (  board[6] == board[7] == board[8] != '_' or # Bottom winner
            board[2] == board[5] == board[8] != '_' # Right column winner
        ):
        winner = board[8]
        print('Winner', winner)
        return winner
    elif (  board[0] == board[1] == board[2] != '_' or # Top row winner
            board[0] == board[3] == board[6] != '_' # Left column winner
        ):
        winner = board[0]
        print('Winner', winner)
        return winner
    elif '_' not in board: # If full board but no winners
        print('Draw!')
        return None
        
while running:
    
    for event in pygame.event.get():

        # Quit if 'X' pressed on window or if 'ESC' is pressed
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        

        # If mouse clicked
        if event.type == pygame.MOUSEBUTTONUP and check_result() == None:
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

                    pygame.display.flip()

                    check_result()
                    
                    # Switch turns between X and O
                    whos_turn = whos_turn ^ 1
                

    





