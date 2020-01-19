import sys
import string

# Some globals
fr = [82, 15, 28, 43, 127, 22, 20, 61, 70, 2, 8, 40, 24, 67, 75, 19, 1, 60, 63, 91, 28, 10, 24, 2, 20, 1]
alphabet = list(string.ascii_lowercase)

#---------Helper functions---------

# reomve non-lowercase from string
def cleanString(string):
    # clean = ""
    # for c in string :
    #     if c in alphabet:
    #         clean += c 
    # return clean    

    clean = [ c for c in string if c in alphabet ]
    return "".join(clean)


# count frequency of letters (*10) 
def getFreqTab(string):
    clean = cleanString(string)

    # ft = []
    # for c in alphabet:
    #     ft.append(int((clean.count(c)*1000)/len(clean)))
    # return ft

    ft = [ int((clean.count(c)*1000)/len(clean)) for c in alphabet ]
    return ft



def chi2 (o, e):
    # r = 0
    # for c in range(len(o)):
    #     r += (o[c]^2 - e[c]^2)/e[c]
    # return r
    return sum( ((o[c]^2 - e[c]^2)/e[c]) for c in range(len(o)) )
  
#---------Main functions---------


# Decode the text
def decode(string):
    # Get frequencies of string
    fs = getFreqTab(string)
    print(fs)
    # Get minimal difference
    found = (0, chi2(fs,fr))
    for i in range(1,26):
        brute = fs[i:]+fs[:i]
        diff = chi2(brute,fr) 
        found = (found[0],found[1]) if diff >= found[1] else (i, diff)

    # decode
    b = alphabet[(26-found[0]):]+alphabet[:(26-found[0])]
    # print(b)
    tr = dict(zip(alphabet,b))

    # decoded = ""
    # for c in string :
    #     decoded += tr[c] if c in tr else c
    # return found[0], decoded
    
    decoded = [tr[c] if c in tr else c for c in string]
    return found[0], "".join(decoded)



#
# Encode the string with custom shift 
#
def encode(n, text):
    # Create translation Dictionary
    b = alphabet[n:]+alphabet[:n]
    # print(alphabet)
    # print(b)
    tr = dict(zip(alphabet,b))
    # print (tr)

    # encoded = ""
    # for c in text :
    #     encoded += tr[c] if c in tr else c
    # return encoded 
    encoded = [ tr[c] if c in tr else c for c in text  ] 
    return "".join(encoded)


def main():

    # Read input file into text
    with open("./input.txt", "r") as fp:  
        text = fp.read()
    print (text, '\n')

    # Get shift
    n = input("Shift ? ")

    # Encode
    encoded = encode(int(n), text)
    print (encoded)

    print ("--------------------------------------------")

    # Decode
    (m, out) = decode (encoded)
    print("Detected shift : ",m)
    print(out)


# ----------------------------------------------------------------------

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
