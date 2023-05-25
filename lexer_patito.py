from ply import *

keywords = (
    'PROGRAM', 'END', 'VAR', 'IF', 'ELSE', 'WHILE', 'DO', 'COUT'
)

tokens = keywords + (
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COLON','LT', 'GT', 'NE',
    'COMMA', 'SCOLON', 'INTEGER', 'FLOAT', 'CTEINT', 'CTEFLOAT', 'CTESTRING',
    'ID'
)

t_ignore= ' \t\n'


def t_REM(t):
    r'REM .*'
    return t


def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t


t_PROGRAM = r'program'
t_END = r'end'
t_VAR = r'var'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_DO = r'do'
t_COUT = r'cout'


t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r'\:'
t_LT = r'<'
t_GT = r'>'
t_NE = r'!='
t_COMMA = r'\,'
t_SCOLON = r';'
t_INTEGER = r'int'
t_FLOAT = r'float'
t_CTEINT = r'\d+'
t_CTEFLOAT = r'\d+\.\d+'
t_CTESTRING = r'".*"'


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lex.lex(debug=0)