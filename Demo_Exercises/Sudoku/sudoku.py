import sys
import time
from pprint import pprint

## Use a multidimensional list to hold the sudoku matrix
sudoku = [[0 for x in range(9)] for y in range(9)]


def load(filename):
    with open(filename, 'r') as f:
        for x in range(9) :
            l = f.readline()[:9]
            for y in range(9):
                sudoku[x][y]=int(l[y])


def present():
    for x in range(9):
        print(sudoku[x])

def check_row(i):
    s = set()
    for y in range(9):
        if sudoku[i][y] > 0 and sudoku[i][y] in s:
            #print("conflict row {}".format(i))
            #print(sudoku[i][y])
            #pprint(s)
            return 1
        s.add(sudoku[i][y])
    return 0

def check_col(i):
    s = set()
    for x in range(9):
        if sudoku[x][i] > 0 and sudoku[x][i] in s:
            #print("conflict col {}".format(i))
            #print(sudoku[x][i])
            #pprint(s)
            return 1
        s.add(sudoku[x][i])
    return 0


def check_sqr(x, y):
    s = set()
    a=int(x/3)*3
    b=int(y/3)*3
    for i in range (a, a+3):
        for j in range (b, b+3):
            if sudoku[i][j] > 0 and sudoku[i][j] in s:
                #print("conflict sqr {}-{}  {}-{}  {}-{} ".format(x,y,a,b,i,j))
                #print(sudoku[i][j])
                #pprint(s)
                return 1
            s.add(sudoku[i][j])
    return 0


def check(x, y):
    error=0
    error += check_row(x)
    error += check_col(y)
    error += check_sqr(x,y)
    if error > 0:
        return False
    return True


def solve():
    #print("entering solve")
    for x in range(9):
        for y in range (9):
            if sudoku[x][y] > 0:
                continue

            for val in range(1,10):
                sudoku[x][y]=val

                #input()
                #time.sleep(0.01)
                #print()
                #present()
                if check(x,y) is False:
                    #print("check is false")
                    continue
                if solve() is False:
                    #print ("solve is False")
                    continue
                return True
            # give up
            sudoku[x][y]=0
            return False
    return True


def main():
    load(sys.argv[1])
    solve()
    present()


if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
