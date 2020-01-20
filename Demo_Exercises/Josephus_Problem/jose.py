#!/usr/bin/python3

import sys
# https://en.wikipedia.org/wiki/Josephus_problem

def main():
    
    assert len(sys.argv) == 3
    n = int(sys.argv[1])+1
    k = int(sys.argv[2])
    assert k > 0
    assert n > k
    
    prisoners = [c for c in range(1,n)]
    pos = k-1

    while len(prisoners) > 1:
        prisoners.pop(pos)
        pos = (pos+k-1)%len(prisoners)
        print(prisoners)


# ------------------------------

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__": 
    main()
