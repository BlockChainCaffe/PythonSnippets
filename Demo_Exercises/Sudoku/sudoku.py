"""
Simple sudoku solver as basic python exercise
This program uses functions, sets, matrix (bidimensional lists)

Requires python3

Usage: python3 sudoku <input-file>

Input file is a text file with nine digits [0-9] per readline
Zero stands for an empty cell in the puzzle to be solved, other
numbers are the constraints given by the puzzle
"""

import sys
import time
from pprint import pprint

## Use a multidimensional list to hold the sudoku matrix
sudoku = [[0 for x in range(9)] for y in range(9)]

## J is the counter of the attempts made (solve iterations)
J=0

def load(filename):
    """ filename: string
    Loads the puzzle from the plain text file
    """
    with open(filename, 'r') as f:
        for x in range(9) :
            l = f.readline()[:9]
            for y in range(9):
                sudoku[x][y]=int(l[y])


def present():
    """Prints the matrix of the sudoku
    Can be used at any time
    """
    for x in range(9):
        print(sudoku[x])

def check_row(i):
    """i: integer, the row to check
    returns: 1 if a duplicate is found, 0 otherwise
    Checks for duplicates in the given row
    """
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
    """i: integer, the row to check
    returns: 1 if a duplicate is found, 0 otherwise
    Checks for duplicates in the given row
    """
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
    """x,y: integers, coordinates of a cell whose 3x3 square has to be checked
    returns: 1 if a duplicate is found, 0 otherwise
    Checks for duplicates in the given 3x3 square
    """
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
    """x,y: integers, coordinates of the cell that changed
    returns: True if the sudoku is legit, False otherwise
    This funcion assumes that the sudoku, without the x,y cell was legit so it
    simply checks the implications of the newly added value.

    """
    error=0
    error += check_row(x)
    error += check_col(y)
    error += check_sqr(x,y)
    if error > 0:
        return False
    return True


def solve():

    """returns: True if the sudoku is solved, False if its not legit
    Solves the sudoku with an recursive algorithm"""
    #print("entering solve")
    global J
    J +=1
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
    print("Number of iterations: {}".format(J) )


if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
