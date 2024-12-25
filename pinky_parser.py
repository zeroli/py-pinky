from tokens import *
from models import *

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens

    def grouping(self):
        pass

    def number(self):
        pass

    def primary(self):
        pass

    def unary(self):
        pass

    def factor(self):
        pass

    def term(self):
        pass

    def expr(self):
        ast = False
        return ast

    def parse(self):
        ast = self.expr()
        return ast
