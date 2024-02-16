"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

test_board = [[EMPTY, EMPTY, O],
            [X, EMPTY, X],
            [O, EMPTY, O]]
test_action = (2,1)

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_O = 0
    count_X = 0
    for row in board:
        for element in row:
            if element == O:
                count_O += 1
            elif element == X:
                count_X += 1
    if count_X == count_O:
        print(X)
        return X
    else:
        print(O)
        return O
        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_elements = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available_elements.add((i,j))
    return available_elements


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    modified_board = copy.deepcopy(board)
    valid = action in actions(modified_board)

    if not valid:
        raise Exception("not allowed")
    
    for i in range(len(modified_board)):
        for j in range(len(modified_board[i])):
            if action == (i, j):
                modified_board[i][j] = player(modified_board)
                # print(modified_board)
                return modified_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY: # Won Vertically
            #print(f"{board[0][i]} Won Vertically")
            return board[0][i]
        elif board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY: # Won Horizontally
            #print(f"{board[i][0]} Won Horizontally")
            return board[i][0]
        elif (board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY: # Won Horizontally
            #print(f"{board[1][1]} Won Diagonally")
            return board[1][1]
            
    #print("Nobody Won") 
    return None

#winner(test_board)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False if winner(board) == None else True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY: # Won Vertically
            won = board[0][i]
        elif board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY: # Won Horizontally
            won = board[i][0]
        elif (board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY: # Won Horizontally
            won = board[1][1]
        else:
            return 0
    return 1 if won == X else -1
             

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    

