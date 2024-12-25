import sys

from tokens import *
from lexer import *
from pinky_parser import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemError("Usage: python pinky.py <script.pinky>")

    filename = sys.argv[1]

    with open(filename) as f:
        source = f.read()

        tokens = Lexer(source).tokenize()
        print("LEXER:")
        for token in tokens:
            print(token)
        print()

        ast = Parser(tokens).parse()
        print("PARSER:")
        print(ast)
