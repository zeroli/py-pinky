# pretty print ast
def pretty_print_ast(ast):
    i = 0
    newline = False

    for ch in str(ast):
        if ch == '(':
            print(ch)
            i += 2
            newline = True
        elif ch == ')':
            if not newline:
                print()
            i -= 2
            print(' ' * i + ch)
            newline = True
        else:
            if newline:
                print(' ' * i, end='')
            print(ch, end='')
            newline = False

class Colors:
    WHITE   = '\033[0m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'

import sys

def lexing_error(msg, lineno):
    print(f'{Colors.RED}[line {lineno}]: {msg}{Colors.WHITE}')
    sys.exit(1)

def parse_error(msg, lineno):
    print(f'{Colors.RED}[line {lineno}]: {msg}{Colors.WHITE}')
    sys.exit(1)
