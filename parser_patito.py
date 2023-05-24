from ply import *
import lexer_patito

tokens = lexer_patito.tokens

precedence = (
    ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Write functions for each grammar rule which is
# specified in the docstring.
def p_programa(p):
    '''
    programa : PROGRAM ID SCOLON vars body END
    '''
    # p is a sequence that represents rule contents.
    #
    # expression : term PLUS term
    #   p[0]     : p[1] p[2] p[3]
    # 
    p[0] = None

def p_vars(p):
    '''
    vars : VAR typed_vars vars
         | empty
    '''
    p[0] = None

def p_typed_vars(p):
    '''
    typed_vars : vars_list COLON type SCOLON typed_vars
               | empty
    '''
    p[0] = None

def p_vars_list(p):
    '''
    vars_list : ID 
              | ID COMMA vars_list
    '''
    p[0] = None

def p_type(p):
    '''
    type : INTEGER
         | FLOAT
    '''
    p[0] = None

def p_body(p):
    '''
    body : LBRACE s RBRACE
    '''
    p[0] = None

def p_s(p):
    '''
    s : statement s
      | empty
    '''
    p[0] = None

def p_statement(p):
    '''
    statement : assign
         | condition
         | cycle
         | print
    '''
    p[0] = None

def p_print(p):
    '''
    print :  COUT LPAREN c m RPAREN SCOLON
    '''
    p[0] = None

def p_c(p):
    '''
    c :  expresion
      |  CTESTRING
    '''
    p[0] = None

def p_m(p):
    '''
    m :  COMMA c m
      |  empty
    '''
    p[0] = None

def p_assign(p):
    '''
    assign :  ID EQUALS expresion SCOLON
    '''
    p[0] = None

def p_cycle(p):
    '''
    cycle :  DO body WHILE LPAREN expresion RPAREN SCOLON
    '''
    p[0] = None

def p_expresion(p):
    '''
    expresion :  exp x
              |  exp
    '''
    p[0] = None

def p_x(p):
    '''
    x : GT exp
      | LT exp
      | NE exp
    '''
    p[0] = None

def p_condition(p):
    '''
    condition : IF LPAREN expresion RPAREN body ELSE body SCOLON
              | IF LPAREN expresion RPAREN body SCOLON
    '''
    p[0] = None


def p_cte(p):
    '''
    cte : CTEINT
        | CTEFLOAT
    '''
    p[0] = None

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | factor_op ID
           | cte
    '''
    p[0] = None

def p_factor_op(p):
    '''
    factor_op : PLUS
              | MINUS
    '''
    p[0] = None

def p_exp(p):
    '''
    exp : termino z
    '''
    p[0] = None

def p_z(p):
    '''
    z : PLUS exp
      | MINUS exp
      | empty
    '''
    p[0] = None

def p_termino(p):
    '''
    termino : factor y
    '''
    p[0] = None

def p_y(p):
    '''
    y : TIMES termino
      | DIVIDE termino
      | empty
    '''
    p[0] = None


def p_empty(p):
    '''empty : '''

def p_error(p):
    if p:
         print("Syntax error at token", p)
         # Just discard the token and tell the parser it's okay.
         parser.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Parse an expression
ast = parser.parse('''

program PATITOS10;

var X:int; J:int;
var Y:float;
{
    X=1+1;

    if (5 > 0) {
        cout("6");
    } else {
        cout("5");
    };

    do {
        cout("hey");
    } while(5>6);

}

end

''')

#print(ast)