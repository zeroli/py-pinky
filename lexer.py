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
        if self.curr + n >= len(self.source):
            return '\0'
        return self.source[self.curr + n]

    def match(self, ch):
        """
        check if `ch` matches with current char and move forward with True returned
        otherwise, return False
        """
        if self.eof():
            return False
        if self.source[self.curr] != ch:
            return False
        self.curr += 1
        return True

    def eof(self):
        """check if scanning beyong the end(EOF)"""
        return self.curr >= len(self.source)

    def add_token(self, token_type):
        self.tokens.append(Token(token_type, self.source[self.start:self.curr], self.line))

    def tokenize(self):
        while self.curr < len(self.source):
            self.start = self.curr
            ch = self.advance()

            if   ch == '\n': self.line += 1
            elif ch == ' ' : pass
            elif ch == '\r': pass
            elif ch == '\t': pass
            elif ch == '#' :
                while not self.eof() and self.peek() != '\n':
                    self.advance()
            elif ch == '+': self.add_token(TOK_PLUS)
            elif ch == '-': self.add_token(TOK_MINUS)
            elif ch == '*': self.add_token(TOK_STAR)
            elif ch == '/': self.add_token(TOK_SLASH)
            elif ch == '(': self.add_token(TOK_LPAREN)
            elif ch == ')': self.add_token(TOK_RPAREN)
            elif ch == '{': self.add_token(TOK_LCURLY)
            elif ch == '}': self.add_token(TOK_RCURLY)
            elif ch == '[': self.add_token(TOK_LSQUAR)
            elif ch == ']': self.add_token(TOK_RSQUAR)
            elif ch == ',': self.add_token(TOK_COMMA)
            elif ch == '.':
                # float number may start with '.': `.323`
                if self.peek().isdigit():
                    self.advance()
                    while self.peek().isdigit():
                        self.advance()
                    self.add_token(TOK_FLOAT)
                else:
                    self.add_token(TOK_DOT)
            elif ch == '^': self.add_token(TOK_CARET)
            elif ch == '%': self.add_token(TOK_MOD)
            elif ch == ';': self.add_token(TOK_SEMICOLON)
            elif ch == '?': self.add_token(TOK_QUESTION)
            elif ch == '=':
                if self.match('='):
                    self.add_token(TOK_EQ)
            elif ch == '~':
                if self.match('='):
                    self.add_token(TOK_NE)
                else:
                    self.add_token(TOK_NOT)
            elif ch == '<':
                if self.match('='):
                    self.add_token(TOK_LE)
                elif self.match('<'):
                    self.add_token(TOK_LTLT)
                else:
                    self.add_token(TOK_LT)
            elif ch == '>':
                if self.match('='):
                    self.add_token(TOK_GE)
                elif self.match('>'):
                    self.add_token(TOK_GTGT)
                else:
                    self.add_token(TOK_GT)
            elif ch == ':':
                if self.match('='):
                    self.add_token(TOK_ASSIGN)
                else:
                    self.add_token(TOK_COLON)
            elif ch == '\'' or ch == '"':
                self.scan_string(ch)
            elif ch.isdigit():
                self.scan_number()
            elif ch.isalpha() or ch == '_':
                self.scan_identifier()

        return self.tokens

    def scan_number(self):
        while self.peek().isdigit():
            self.advance()
        if self.peek() == '.':
            self.advance()  # consume '.'
            while self.peek().isdigit():
                self.advance()
            self.add_token(TOK_FLOAT)
        else:
            self.add_token(TOK_INTEGER)

    def scan_string(self, start_quote):
        while not self.eof() and self.peek() != start_quote:
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        if self.eof():
            raise SyntaxError(f"line {self.line} not closed with quote `{start_quote}` for string")
        self.advance()
        # strip the start/end quote
        self.start += 1
        self.curr -= 1
        self.add_token(TOK_STRING)
        self.advance()
        self.advance()

    def scan_identifier(self):
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()
        text = self.source[self.start:self.curr]
        keyword_type = keywords.get(text)
        if not keyword_type:
            self.add_token(TOK_IDENTIFIER)
        else:
            self.add_token(keyword_type)
