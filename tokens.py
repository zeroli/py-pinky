TOK_PLUS       = 'TOK_PLUS'
TOK_MINUS     = 'TOK_MINUS'
TOK_MUL        = 'TOK_MUS'
TOK_DIV         = 'TOK_DIV'

class Token(object):
    def __init__(self, token_type, lexme, line):
        self.token_type = token_type
        self.lexme = lexme
        self.line = line

    def __repr__(self):
        return f'({self.token_type}, {self.lexme!r}, {self.line})'
