"""
Tic Tac Toe Player
"""
import random
import math
import copy
from functools import reduce
X = "X"
O = "O"
EMPTY = None


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
    ##print(player(board), "player")
    # #print("boardds", board)
    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                counter += 1

    if counter == 9:
        return X
    if counter % 2 == 0:
        return O
    else:
        return X

    # my notes are: set the function of the next player, try to make some moves


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ##print("actions")
    avai = []
    for i in range(3):
        temp = []
        for k in range(3):
            if board[i][k] == None:
                can1 = tuple([i, k])
                temp.append(can1)
            if k == 2:
                if temp:
                    avai.append(temp)

    return avai
    ##print("actions", avai)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ##print("result")
    ##print("action")
    """if action[0] != (0 or 1) or action[1] != (0 or 1):
        #print("not exsist")"""
    ##print("hey")
    ##print( "hey",Max_Value(board))
    new_board = copy.deepcopy(board)
    #new_board = board.copy()
    for i in range(3):
        for k in range(3):
            if new_board[i][k] == None: #or if .... in actions(board)
                can1 = tuple([i, k])
                if tuple([i, k]) == action:
                    new_board[i][k] = player(board)
                    ##print(player(board), "new board =", new_board)
                    return new_board





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    ##print("winner")
    i = k = 0
    list = [(i, k), (k, i)]
    for item in range(2):
        # #print("ROUND ", item)
        tmp = 0
        for i in range(3):
            win = []
            for k in range(3):  # #print( "B", i, k, end=" and ")
                if item == 1:
                    # #print("B", i, k)
                    i ^= k
                    k ^= i
                    i ^= k
                """if board[i][k] == None:#tTODO
                    continue"""
                con = first_item = nxt = None
                if item == 1:
                    con = i < len(board) - 1
                    if con:
                        nxt = board[i + 1][k]
                    first_item = board[0][k]

                if item == 0:
                    con = k < len(board) - 1
                    if con:
                        nxt = board[i][k + 1]
                    first_item = board[i][0]
                if con:
                    if board[i][k] == nxt:
                        tmp = board[i][k]
                else:
                    if board[i][k] == first_item and tmp != 0:
                        tmp = board[i][k]
                    else:
                        tmp = 0

                # #print("t",i,k,"=",tmp)
                """if tmp == 0:
                     k ^= i
                    i ^= k
                    k ^= i
                    continue"""
                if tmp != 0 and tmp != None:
                    win.append(tmp)
                if len(win) == 3:
                    if win[0] == X:
                        return X
                    elif win[0] == O:
                        return O

                    return None
                if item == 1:
                    # #print(i, k)
                    k ^= i
                    i ^= k
                    k ^= i

                #cross
                if board[0][0] == board[1][1] == board[2][2]:
                    if board[0][0] == X:
                        return X
                    elif board[0][0] == O:
                        return O
                    else:
                        return None
                if board[2][0] == board[1][1] == board[0][2]:
                    if board[2][0] == X:
                        return X
                    elif board[2][0] == O:
                        return O
                    else:
                        return None

    #return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    ##print("terminal")
    # #print("winnar", winner(board))
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                # #print("In progess game")
                return False
    return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ##print("utility", utility(board))
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    can1 = []
    can = []

    if reduce(lambda count, l: count + len(l), actions(board), 0) >= 8:  # tmp
        for listy in actions(board):
            for movee in listy:
                can.append(movee)
        if player(board) == X:
            return random.choice(can)
        else:
            return random.choice(can)
    else:
        if player(board) == X:
            #print("1")
            score = -math.inf
            bestmove = None
            for listy in actions(board):
                for movee in listy:
                    can.append(movee)
            for action in can:
                re = min_value(result(board, action))
                if re > score:
                    score = re
                    bestmove = action
            #print("111111111111111111111111111111111111111111111111111111111111111111 best",player(board), best)
            return bestmove

        elif player(board) == O:
            #print("2")

            score = math.inf
            bestmove = None
            for listy in actions(board):
                for movee in listy:
                    can1.append(movee)

            for action in can1:
                #print("2- round action =", action)
                re = max_value(result(board, action))

                if re < score:
                    ##print("2 sore and currend",score,current)
                    score = re
                    bestmove = action
            #print("222222222222222222222222222222222222222222222222222222222222222222222 best",player(board), best)
            return bestmove


def max_value(board):
    #print("3",board)
    if terminal(board):
        #print("3 term")
        return utility(board)
    v = -math.inf
    can = []
    for listy in actions(board):
        for movee in listy:
            can.append(movee)
    for action in can:
        #print("3- round action =", action)
        ##print("-",action, result(board, action), max_value(result(board, action)))
        v = max(v, min_value(result(board, action)))
    #print("3 v =", v)
    return v

def min_value(board):
    #print("4", board)
    if terminal(board):
        #print("4 term", utility(board))
        return utility(board)
    v = math.inf
    can = []
    for listy in actions(board):
        for movee in listy:
            can.append(movee)
    for action in can:
        #print("4- round action =", action)
        #print(action,result(board, action),max_value(result(board, action)))
        v = min(v, max_value(result(board, action)))
    #print("4v", v)
    return v

