import sys
import string

# Some globals
fr = [82, 15, 28, 43, 127, 22, 20, 61, 70, 2, 8, 40, 24, 67, 75, 19, 1, 60, 63, 91, 28, 10, 24, 2, 20, 1]
alphabet = list(string.ascii_lowercase)


def cleanString(string):
    clean = ""
    for c in string :
        if c in alphabet:
            clean += c 
    return clean   

def getFreqTab(string):
    clean = cleanString(string)
    ft = []
    for c in alphabet:
        p = (clean.count(c)*1000)/len(clean)
        ft.append(int(p))
        # ft.append(int((clean.count(c)*1000)/len(clean)))
    return ft

def decode(string):
    fs = getFreqTab(string)
    print(fs)


def encode(n, text):
    print(alphabet)
    print(n)
    b = alphabet[n:]+alphabet[:n]
    tr = dict(zip(alphabet,b))

    encoded = ""
    for c in text :
        encoded += tr[c] if c in tr else c
    return encoded 

def main():
    # Read input file into text
    with open("./input.txt", "r") as fp:  
        text = fp.read()
    print (text, '\n')

    # Get shift
    n = input("Shift ? ")
    
    # Encode
    encoded = encode(int(n),text)
    print(encoded)

    # Decode
    (m,out) = decode(encoded)
    print("Detected shift : ",m)
    print(out)

# ----------------------------------------------------------------------

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
