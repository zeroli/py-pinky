from tokens import *

class Expr(object):
    '''
    example: 3 + (3 * 4) + (32 * - 30)
    '''
    pass

class Stmt(object):
    '''
    statements perform actions
    '''
    pass

class Integer(Expr):
    '''
    example: 7
    '''
    def __init__(self, value):
        assert isinstance(value, int), value
        self.value = value

    def __repr__(self):
        return f'Integer[{self.value}]'

class Float(Expr):
    '''
    example: 3.23
    '''
    def __init__(self, value):
        assert isinstance(value, float), value
        self.value = value

    def __repr__(self):
        return f'Float[{self.value}]'

class Ident(Expr):
    '''
    example: x
    '''
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Ident[{self.value}]'

class UnOp(Expr):
    '''
    example: -10
    '''
    def __init__(self, op: Token, operand: Expr):
        assert isinstance(op, Token), op
        assert isinstance(operand, Expr), operand
        self.op = op
        self.operand = operand

    def __repr__(self):
        return f'({self.op.lexeme} {self.operand})'


class BinOp(Expr):
    '''
    example: 3 * 4
    '''
    def __init__(self, op: Token, left: Expr, right: Expr):
        assert isinstance(op, Token), op
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.op.lexeme} {self.left} {self.right})'

class Group(Expr):
    '''
    example: ( <expr> )
    '''
    def __init__(self, expr: Expr):
        self.expr = expr

    def __repr__(self):
        return f'({self.expr})'
