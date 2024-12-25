from tokens import *

class Lexer(object):
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.curr = 0
        self.line = 1
        self.tokens = []

    def advance(self):
        ch = self.source[self.curr]
        self.curr += 1
        return ch

    def peek(self):
        return self.source[self.curr]

    def lookahead(self, n=1):
        return self.source[self.curr + n]

    def consume(self, ch):
        if self.source[self.curr] != ch:
            return False
        self.curr += 1
        return True

    def add_token(self, token_type):
        self.tokens.append(Token(token_type, self.source[self.start:self.curr], self.line))

    def tokenize(self):
        while self.curr < len(self.source):
            self.start = self.curr
            ch = self.advance()

            if    ch == '\n': self.line += 1
            elif ch == ' ':   pass
            elif ch == '\r': pass
            elif ch == '\t': pass
            elif ch == '+': self.add_token(TOK_PLUS)
            elif ch == '-': self.add_token(TOK_MINUS)
            elif ch == '*': self.add_token(TOK_MUL)
            elif ch == '/': self.add_token(TOK_DIV)

        return self.tokens
