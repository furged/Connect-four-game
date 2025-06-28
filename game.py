import numpy as np # numerical computing library 

def create_board():
    board = np.zeros((6,7))  # , dtype = int) can also be added if we want integer zeros [0 instead of 0.]
    # zeros() is a method of np which creates a numpy array .. the shape is gonna be 6 rows and 7 columns. refer the output to see what it looks like 
    return board

# define a function to actually drop a piece:
def drop_piece():
    pass

# this function is to check that if the location entered by thhe palyer is valid and its gonna check if the top row of that column is still emoty or not
def is_valid_location(board, col):
    return board[5][col] == 0 # if this is true then we're good to let the player drop the piece in that column otherwise not
    

def get_next_open_row():
    pass

""" 
to see what the board looks like:
board = create_board()
print(board)
"""

board = create_board()
game_over = False # will only switch to true when someone gets 4 in a row
turn = 0 # to track that which players turn is it

while not game_over:
    # ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6):"))   

        

    # ask for player 2 input
    else:
        col = int(input("Player 2 Make your Selection (0-6):")) 

    # and now no matter whos turn it was we're gonna have to increase turn by 1
    turn += 1
    turn = turn % 2 # this will make the turn alternate bw 0 and 1 so 0 would be player 1 turn and 1 would be player 2 turn
