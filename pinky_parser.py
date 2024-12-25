from tokens import *
from models import *

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr = 0
        self.prev_token = None

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
            if not self.match(TOK_RPAREN):
                raise SyntaxError(f'Expected ")" to close')
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

    def parse(self):
        ast = self.expr()
        return ast

    def match(self, token_type):
        if self.curr >= len(self.tokens):
            return False
        if self.tokens[self.curr].token_type != token_type:
            return False
        self.prev_token = self.tokens[self.curr]
        self.curr += 1
        return True

    def previous_token(self):
        return self.prev_token
