"""
Simple sudoku solver as basic python exercise
This program uses functions, sets, matrix (bidimensional lists)

Requires python3

Usage: python3 sudoku <input-file>

Input file is a text file with nine digits [0-9] per readline
Zero stands for an empty cell in the puzzle to be solved, other
numbers are the constraints given by the puzzle

This second version is about 40% faster and 30% shorter

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


def possible_values(x,y):
    """x,y: integers, the coordinates of the cell to get possible values for"""
    s = set()
    s = {1,2,3,4,5,6,7,8,9}

    for i in range(9):
        s.discard(sudoku[i][y])
    for j in range(9):
        s.discard(sudoku[x][j])
    a=int(x/3)*3
    b=int(y/3)*3
    for i in range (a, a+3):
        for j in range (b, b+3):
            s.discard(sudoku[i][j])
    return s

def solve():
    """returns: True if the sudoku is solved, False if its not legit
    Solves the sudoku with an recursive algorithm
    This version better than the previous one as it
    limits the values to try to the legit ones, and reduces the need
    to check the sudoku multiple times"""
    #print("entering solve")
    global J
    J +=1
    for x in range(9):
        for y in range (9):
            if sudoku[x][y] > 0:
                continue

            s=possible_values(x,y)
            for val in s:
                sudoku[x][y]=val
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
