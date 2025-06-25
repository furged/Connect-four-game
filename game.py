import numpy as np # numerical computing library 

def create_board():
    board = np.zeros((6,7))  # , dtype = int) can also be added if we want integer zeros [0 instead of 0.]
    # zeros() is a method of np which creates a numpy array .. the shape is gonna be 6 rows and 7 columns. refer the output to see what it looks like 
    return board

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

    # ask for player 2 input