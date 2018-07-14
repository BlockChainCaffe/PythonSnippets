"""
HELLO PROFESSOR FALKEN
SHALL WE PLAY A GAME ?

"""

import sys
import os

board = [[0 for x in range(3)] for y in range(3)]
win = 3**2

def draw_board():
    # os.system("clear")
    print("")
    print("")
    print("")
    for x in range(3):
        for y in range(3):
            print(" ",end="")
            print( { -1:'O', 1:'X', 0:' ' }.get(board[x][y]),end="" )
            print(" ",end="")
            if y<2 : print("|",end="")
        print("")
        if x<2 : print("---+---+---")


def score_col(i):
    score=0
    for x in range(3):
        score+=board[x][i]
    #print("score of col {} : {} ".format(i,score))
    return score**2

def score_row(i):
    score=0
    for y in range(3):
        score+=board[i][y]
    #print("score of row {} : {} ".format(i,score))
    return score**2

def score_dia(i):
    score=0
    for y in range(3):
        # i=0 --> 0,1,2
        # i=1 --> 2,4,6 --> 2,1,0
        x=(y+(i*(y+2)))%3
        score+=board[x][y]
    #print("score of dia {} : {} ".format(i,score))
    return score**2


def winner():
    """Checks if one of the player won the game"""
    for x in range(3):
        score=score_col(x)
        if (score==win): return 1
        if (score==-1*win): return -1

    for y in range(3):
        score=score_row(y)
        if (score==win): return 1
        if (score==-1*win): return -1

    for d in range(2):
        score=score_dia(d)
        if (score==win): return 1
        if (score==-1*win): return -1
    return 0



def board_balance():
    balance=0
    for i in range(3):
        balance+=score_col(i)
        balance+=score_row(i)
    for d in range(2):
        balance+=score_dia(d)
    print("balance : {} ".format(balance))
    return balance



def gameover():
    """Checks if the game is over by:
    a: there is a winner
    b: the board is full
    """
    # search an empty cell
    for j in range(9):
        if board[int(j/3)][int(j%3)]==0 : break
    else: return True
    # check for a winner
    if winner()!=0 : return True
    return False


def ai():
    """OK, callint it AI is a bit too much, but that's my my code."""
    moves=[100 for x in range(9)]
    now=board_balance();
    # Evaluate all possible moves left
    for j in range(9):
        x=int(j/3)
        y=int(j%3)
        if board[x][y]!=0 : continue
        print(j)
        board[x][y]=-1
        moves[j]=board_balance();
        board[x][y]=0

    best=min(moves)
    print("best : {}".format(best))
    for k in range(9):
        if moves[k]==best :
            j=k
            break
    x=int(j/3)
    y=int(j%3)
    board[x][y]=-1



def playermove():
    M=int(input("Your move? (1:9)"))-1
    x=int(M/3)
    y=int(M%3)
    board[x][y]=1


def main():
    while not gameover():
        draw_board()
        playermove()
        if not gameover():
            draw_board()
            ai()
    draw_board()
    if winner()==1:
        print ("you win!")
    else:
        print ("I win!")





if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
