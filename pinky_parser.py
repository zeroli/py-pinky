from tokens import *
from models import *
from utils import *

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr = 0 # next token position

    # parsing entrance
    def parse(self):
        ast = self.expr()
        return ast

    def grouping(self):
        return Group(self.expr())

    def interger(self):
        return Integer(int(self.previous_token().lexeme))

    def float(self):
        return Float(float(self.previous_token().lexeme))

    def ident(self):
        return Ident(self.previous_token().lexeme)

    def primary(self):
        '''
        <primary> ::= <integer>
                    | <float>
                    | <identitifer>
                    | '(' <expr> ')'
        '''
        if self.match(TOK_INTEGER):
            return self.interger()
        if self.match(TOK_FLOAT):
            return self.float()
        if self.match(TOK_IDENTIFIER):
            return self.ident()
        if self.match(TOK_LPAREN):
            expr = self.expr()
            self.expect(TOK_RPAREN)
            return Group(expr)

    def unary(self):
        '''
        <unary> ::= ('-' | '+' | '~') <unary>
                  | <primary>
        '''
        if self.match(TOK_MINUS) or self.match(TOK_PLUS) or self.match(TOK_NOT):
            op = self.previous_token()
            expr = UnOp(op, self.unary())
        else:
            expr = self.primary()
        return expr

    def factor(self):
        '''
        <factor> ::= <unary>
        '''
        return self.unary()

    def term(self):
        '''
        <term> ::= <factor> (('*' | '/') <factor>)*
        '''
        factor = self.factor()

        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.factor()
            factor = BinOp(op, factor, right)
        return factor

    def expr(self):
        '''
        <expr> ::= <term> (('+' | '-') <term>)*
        '''
        term = self.term()

        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op = self.previous_token()
            right = self.term()
            term = BinOp(op, term, right)
        return term

    # ######################
    # helper functions
    # ######################
    def match(self, token_type):
        '''
        test if current token matches with given one
        if matches, consume current token, and advance to next token as well, and return True
        otherwise, return False
        '''
        if self.curr >= len(self.tokens):
            return False
        if not self.peek_match(token_type):
            return False
        self.advance()
        return True

    def expect(self, token_type):
        '''
        test if current token matches with given one
        if matches, consume/return current token, and advance to next token as well
        otherwise, raise error
        '''
        if self.curr >= len(self.tokens):
            parse_error(f'Expect {token_type!r}, EOF encountered', self.previous_token().line)
        if not self.match(token_type):
            parse_error(f'Expect {token_type!r}, found {self.peek().lexeme!r}', self.peek().line)
        return self.previous_token()

    def advance(self):
        '''
        consume/return current token, and advance to next token
        '''
        if self.curr >= len(self.tokens):
            return Token(TOK_EOF, '')
        self.curr += 1
        return self.previous_token()

    def peek(self):
        '''
        peek/return next token without consuming it
        '''
        return self.tokens[self.curr]

    def peek_match(self, token_type):
        '''
        peek next token and test if it matches with given one
        return True if matches, without consume/advance
        return False if no match
        '''
        return self.peek().token_type == token_type

    def previous_token(self):
        return self.tokens[self.curr - 1]
