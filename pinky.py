import sys

from tokens import *
from lexer import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemError("Usage: python pinky.py <script.pinky>")

    filename = sys.argv[1]

    with open(filename) as f:
        source = f.read()

        tokens = Lexer(source).tokenize()
        for token in tokens:
            print(token)
