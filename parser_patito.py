from ply import *
import lexer_patito

tokens = lexer_patito.tokens

precedence = (
    ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

variableDict = {}

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
    
    if len(p) == 2:
        p[0] = None
    else:
        for i in range(1, len(p)):
            if(p[i] == 'var'):
                vars = p[i+1]
                temp = ""
                char_var = 0
                while char_var < len(vars):
                    if vars[char_var] == ':' and temp != "":

                        if temp in variableDict:
                                print("Error: DOBLE VARIABLE DECLARATION")
                                raise SystemExit
                        else:  
                            if vars[char_var+1] == 'f':
                                    variableDict[temp] = 'float'
                                    char_var+=6
                                    temp = ""
                            else:
                                variableDict[temp] = 'int'
                                char_var+=4
                                temp = ""
                        

                    if(vars[char_var] != ";" and vars[char_var] != ":"):
                        temp += vars[char_var]
                    char_var+=1
       
    

def p_typed_vars(p):
    '''
    typed_vars : vars_list COLON type SCOLON typed_vars
               | empty
    '''
    
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[1]
        for i in p:
            if i != None and i!=p[0]:
                p[0] += i

def p_vars_list(p):
    '''
    vars_list : ID 
              | ID COMMA vars_list
    '''

    p[0] = p[1]


def p_type(p):
    '''
    type : INTEGER
         | FLOAT
    '''
    
    p[0] = p[1]

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
    c :  expr
      |  relexpr
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
    assign :  ID EQUALS expr SCOLON
    '''

    if p[1] not in variableDict:
        print("Syntax Error: VARIABLE NOT DECLARED (SHOULD BE DECLARED OUTSIDE OF BODY)")
        raise SystemExit

    p[0] = None

def p_cycle(p):
    '''
    cycle :  DO body WHILE LPAREN relexpr RPAREN SCOLON
    '''
    p[0] = None

def p_expr_operations(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''

    p[0] = ('BINOP', p[2], p[1], p[3])


def p_expr_number(p):
    '''expr : INTEGER
            | FLOAT'''
    p[0] = ('NUM', eval(p[1]))


def p_expr_variable(p):
    '''expr : ID'''

    if p[1] not in variableDict:
        print("Syntax Error: VARIABLE NOT DECLARED (SHOULD BE DECLARED OUTSIDE OF BODY)")
        raise SystemExit

    p[0] = ('VAR', p[1])

def p_expr_constant(p):
    '''expr : cte'''
    p[0] = ('CTEVAL', p[1])

def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = ('GROUP', p[2])


# Relational expressions


def p_relexpr(p):
    '''relexpr : expr LT expr
               | expr GT expr
               | expr EQUALS expr
               | expr NE expr'''
    p[0] = ('RELOP', p[2], p[1], p[3])



def p_condition(p):
    '''
    condition : IF LPAREN relexpr RPAREN body ELSE body SCOLON
              | IF LPAREN relexpr RPAREN body SCOLON
    '''
    p[0] = None


def p_cte(p):
    '''
    cte : CTEINT
        | CTEFLOAT
    '''
    p[0] = None


def p_empty(p):
    '''empty : '''

def p_error(p):
    if p:
         print("Syntax error at token", p)
         # Just discard the token and tell the parser it's okay.
         #parser.errok()
    else:
         print("Syntax error at EOF")

def reset_variables():
    global variableDict
    variableDict = {}

# Build the parser
parser = yacc.yacc()

#print(variableDict)
#print(ast)