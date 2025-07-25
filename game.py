import numpy as np 
import pygame 
import sys
import math

PINK = (255, 192, 203)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 105, 97)


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))  # , dtype = int) -> [0 instead of 0.]
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece 

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 
    
def get_next_open_row(board, col):
    for r in range(ROW_COUNT): 
        if board[r][col] == 0:
            return r 

def print_board(board):
    print(np.flip(board, 0)) # 0 is for vertical flip and 1 is for horizontal flip and "None" is for both combined
    
def winning_move(board, piece):
    # Horizontal 
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and  board[r][c+2] == piece and  board[r][c+3] == piece:
                return True
            
    # Vertical
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT -3):
            if board[r][c] == piece and board[r+1][c] == piece and  board[r+2][c] == piece and  board[r+3][c] == piece:
                return True
            
    # Positive slope diagonal
    for c in range (COLUMN_COUNT-3): 
        for r in range(ROW_COUNT -3):
            if board[r][c] == piece and board[r+1][c+1] == piece and  board[r+2][c+2] == piece and  board[r+3][c+3] == piece:
                return True

    # Negative slope diagnonal
    for c in range (COLUMN_COUNT-3): 
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and  board[r-2][c+2] == piece and  board[r-3][c+3] == piece:
                return True

def draw_board(board):
    screen.fill((255, 255, 255)) 
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, PINK, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height-int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height-int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

board = create_board() 
print_board(board)
game_over = False 
turn = 0 

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

RADIUS = int(SQUARESIZE/2 - 5)

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
             
            if turn == 0:
                posx = event.pos[0]

                col = int(posx//SQUARESIZE)
                row = get_next_open_row(board, col)
  
                drop_piece(board, row, col, 1)

                if winning_move(board, 1): 
                    print("Player 1 Wins!")
                    game_over = True
                
            else:
                posx = event.pos[0]

                col = int(posx//SQUARESIZE)
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("Player 2 Wins!")
                    game_over = True
                

            print_board(board)
            draw_board(board)
            
            turn += 1
            turn = turn % 2 
