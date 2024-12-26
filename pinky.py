import sys

from tokens import *
from lexer import *
from pinky_parser import *
from utils import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemError("Usage: python pinky.py <script.pinky>")

    filename = sys.argv[1]

    with open(filename) as f:
        source = f.read()

        tokens = Lexer(source).tokenize()
        print(f'{Colors.GREEN}LEXER:{Colors.WHITE}')
        for token in tokens:
            print(token)
        print()

        ast = Parser(tokens).parse()
        print(f'{Colors.GREEN}PARSED AST:{Colors.WHITE}')
        pretty_print_ast(ast)
