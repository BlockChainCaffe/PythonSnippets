import sys

def decode(string):
    return "a"

def encode(n, text):
    return "a"

def main():
    text=""
    n=3

    encoded = encode(n,text)
    print(encoded)

    out = decode(encoded)
    print(out)

# ----------------------------------------------------------------------

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__":
        main()
