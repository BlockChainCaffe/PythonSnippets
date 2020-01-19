import sys
import string

# Some globals
alphabet = list(string.ascii_lowercase)

def decode(string):
    return "a"

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
