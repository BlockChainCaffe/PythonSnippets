"""
HELLO PROFESSOR FALKEN
SHALL WE PLAY A GAME ?
"""
import sys
import os

board = [[0 for x in range(3)] for y in range(3)]
WIN = 100
checklines =(
                ( (0,0),(0,1),(0,2) ), ( (1,0),(1,1),(1,2) ), ( (2,0),(2,1),(2,2) ), 
                ( (0,0),(1,0),(2,0) ), ( (0,1),(1,1),(2,1) ), ( (0,2),(1,2),(2,2) ), 
                ( (0,0),(1,1),(2,2) ), ( (0,2),(1,1),(2,0) ) 
            )

def draw_board():
    os.system("clear")
    print("\n\n\n")
    for x in range(3):
        for y in range(3):
            print(" "+{ -1:'O', 1:'X', 0:' ' }.get(board[x][y])+" ", end="" )
            if y<2 : print("|",end="")
        if x<2 : print("\n---+---+---")

def the_score(score,zeros):
    if abs(score)==3 : return WIN*(score/abs(score))
    if zeros==0 or score==0 : return 0
    return score*abs(score)*abs(score)

def score_line(line):
    score, zeros = 0,0
    for cell in line:
        score += board[cell[0]][cell[1]]
        if board[cell[0]][cell[1]] == 0 : zeros += 1
    return the_score(score,zeros)

def winner():
    """Checks if one of the player won the game"""
    for line in checklines:
        score = score_line(line)
        if (score==WIN): return 1
        if (score==-1*WIN): return -1
    # no winner
    return 0

def board_balance():
    balance=0
    for line in checklines:
        balance+=score_line(line)
    return balance

def gameover():
    """Checks if the game is over by:
    a: there is a winner
    b: the board is full
    """
    # search an empty cell
    for(x,y) in [(x,y) for x in range(3) for y in range(3)]:    # Notice the for/else instruction
        if board[x][y]==0 : break                               # Needs a break inside
    else: return True                                           # Else is executed if did not break out from loop
    # check for a winner
    return winner() != 0

def ai():
    """OK, calling it AI is a bit too much, but that's my code."""
    X,Y = 0,0
    bestmove=WIN

    for (x,y) in [(x,y) for x in range(3) for y in range(3)]:
        if board[x][y]!=0 : continue
        board[x][y]=-1
        move=board_balance()
        board[x][y]=1
        move-=board_balance()
        board[x][y]=0
        if move < bestmove:
            bestmove=move
            (X,Y)=(x,y)

    board[X][Y]=-1

def playermove():
    print("")
    while True:
        M=int(input("\n\nYour move? (1:9)"))-1
        x=int(M/3)
        y=int(M%3)
        if board[x][y] == 0 : break
    board[x][y]=1

def main():
    while not gameover():
        draw_board()
        playermove()
        if not gameover():
            ai()

    draw_board()
    print ("\n "+{-1: "I Win !", 1: "You Win !", 0: "Draw !"  }.get(winner()))

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
