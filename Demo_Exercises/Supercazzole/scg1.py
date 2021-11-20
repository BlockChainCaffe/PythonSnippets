'''

Generatore di supercazzole su base statistica

Credits:
    Vocabolario di partenza : https://github.com/napolux/paroleitaliane

'''

### Imports

import string
import json
import sys
from random import seed
from random import randint
import copy


### Functions

def filterLetter(word):
    word = word.lower()
    w2 = list(filter( lambda l : l in string.ascii_lowercase , word))
    return ''.join(w2)

def getStartKeys():
    keys = [ ""+a+b+c+"" for a in string.ascii_lowercase for b in string.ascii_lowercase for c in string.ascii_lowercase]
    return keys


def getEmptyLFS ():
    ''' Definizione della struttura probabilistica vuota '''
    # lista di tutti gli insiemi di stringe
    keys = getStartKeys()
    next = { letter : 0 for letter in string.ascii_lowercase }
    # struttura
    lfs = { key : { 'starter': 0, 'ender': 0, 'next': copy.copy(next) } for key in keys }
    return lfs


def saveLFS(filename, lfs1):
    ''' Salva la struttura di frequenza delle lettere in un file '''
    string = json.dumps(lfs1)
    with open(filename,"w") as f:
        f.write(string)


def loadLFS(filename):
    ''' Carica la struttura di frequenza di lettere in un file '''
    j = {}
    with open(filename, 'r') as f:
        string = f.read()
        j = json.read()
    return j


def composeLFS(vocabulary):
    ''' Riempie una struttura LFS con i dati provenienti da un vocabolario
    di una data lingua.
    Il vocabolario deve essere fatto mettendo ogni parola su una riga diversa
    in formato testo semplice (txt) '''

    lfs = getEmptyLFS()
    with open(vocabulary, 'r') as voc:
        word = voc.readline()
        while word :
            word = filterLetter(word)
            begin = word[0:3]
            end = word[-3:]
            lfs[begin]['starter'] +=1
            lfs[end]['ender'] += 1
            for p in range(len(word)-3) :
                idx = word[p:p+3]
                lfs[idx]['next'][word[p+3]] += 1
            word = voc.readline()
    return lfs


def create(lfs1):
    ''' Crea una supercazzola a partire dalle statiche dell lfs fornito '''
    word = ''
    keys = getStartKeys()
    #  startsum = reduce ( (lambda entry, sum : sum + entry['starter']) , lfs1)
    startsum = sum( [ lfs1[k]['starter'] for k in keys] )
    startpos = randint(0,startsum+1)

    ## estrae le prime 2 lettere
    start = ''
    for i in keys:
        start = i
        startpos -= lfs1[i]['starter']
        if (startpos <= 0):
            break
    word += start

    while True:
        ## estrae la prossima lettera
        nextsum = sum(lfs1[start]['next'].values())
        nextsum += lfs1[start]['ender']
        nextpos = randint(0,nextsum+1)
        next = ''
        for i in string.ascii_lowercase:
            next = i
            nextpos -= lfs1[start]['next'][i]
            if (nextpos <= 0):
                break
        # Endend ?
        if (nextpos > 0):
            return word
        word += next
        start = word[-3:]


def main():
    wordfile = sys.argv[1]
    lfs = composeLFS(wordfile)
    sup = create(lfs)
    print(sup)





if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
