from ply import *
import lexer_patito
from queue import Queue

tokens = lexer_patito.tokens

precedence = (
    ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

variableDict = {}
# Initializing a queue
quadruples = []
temps = []
pendinglocs = []

def p_programa(p):
    '''
    programa : PROGRAM ID SCOLON vars body END
    '''
    global quadruples
    p[0] = p[5]
    quadruples.append([len(quadruples)+1,"END"])

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
    body : LBRACE listofstatements RBRACE
    '''


def p_s(p):
    '''
    listofstatements : statement listofstatements
                     | empty
    '''

def p_statement(p):
    '''
    statement : assign
              | condition
              | cycle
              | print
    '''

    p[0] = p[1]

pendingPrints = []
def p_print(p):
    '''
    print :  COUT LPAREN listedexpr RPAREN SCOLON
    '''
    global pendingPrints
    pendingPrints.append(p[3])
    quadruples.append([len(quadruples)+1,"PRINT", "p" + str(len(pendingPrints))])
    p[0] = ("PRINT", p[3])


def p_listedexpr(p):
    '''
    listedexpr :  c
               |  c COMMA c m
        
    '''
    global listexpr
    listexpr.reverse()
    #print(p[4])
    if(len(p) > 2 ):
        listexpr.insert(0, p[3])
        listexpr.insert(0, p[1])
        p[0] = listexpr
        listexpr = []
    else:
        p[0] = p[1]   

def p_c(p):
    '''
    c :  ID
      |  cte
      |  CTESTRING

    '''
    p[0] = (p[1])
        
listexpr = []
def p_m(p):
    '''
    m :  COMMA c m
      |  empty
    '''

    if(len(p) > 2):
        listexpr.append(p[2])

def p_assign(p):
    '''
    assign :  ID EQUALS expr SCOLON
    '''

    if p[1] not in variableDict:
        print("Syntax Error: VARIABLE NOT DECLARED (SHOULD BE DECLARED OUTSIDE OF BODY)")
        raise SystemExit
    
    global temps
    if(len(p[3]) == 2 and isinstance(p[3], tuple) and len(p[3][1]) == 1 ):
        #print("Yo fui el culpable alv: ", p[3], "Len: ", len(p[3]))
        #print("1: ", p[3][0], "2: ", p[3][1], "\n\n")
        quadruples.append([len(quadruples)+1,p[2], p[1], p[3][1]])
    elif(isinstance(p[3], str)):
        quadruples.append([len(quadruples)+1,p[2], p[1], p[3]])
    else:
        print("Ando perdido", p[3], len(p[3]))
    p[0] = ("ASSIGN", p[1], p[3])

def p_cycle(p):
    '''
    cycle :  do body WHILE LPAREN relexprcycle RPAREN SCOLON
    '''

    p[0] = ("CYCLE", p[2], p[5])

def p_cycle_do_mark(p):
    '''
    do :  DO 
    '''

    global quadruples
    global pendinglocs
    pendinglocs.append(len(quadruples)+1)

    p[0] = p[1]

def p_expr_operations(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''
    
    #print("P1: ", p[1], "Length: ", len(p[1]), "P3: ", p[3], "Length: ", len(p[3]))

    global quadruples
    global temps
    if(len(p[1]) == 2 and len(p[3])== 2 and isinstance(p[1], tuple) and isinstance(p[3], tuple)):
        #print("P1: ", p[1], "Length: ", len(p[1]), "\nP3: ", p[3], "Length: ", len(p[3]))
        quadruples.append([len(quadruples)+1, p[2], p[1][1], p[3][1], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    elif(isinstance(p[1], str) and isinstance(p[3], str)):
        quadruples.append([len(quadruples)+1, p[2], p[1], p[3], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    elif(len(p[3])== 2 and isinstance(p[1], str)):
        quadruples.append([len(quadruples)+1, p[2], p[1], p[3][1], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    elif(len(p[1]) == 2 and isinstance(p[3], str)):
        quadruples.append([len(quadruples)+1, p[2], p[1][1], p[3], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    else:
        p[0] = ('BINOP', p[2], p[1], p[3])
        print(p[0])
    
    
def p_expr_variable(p):
    '''expr : ID
            | LPAREN ID RPAREN'''

    if len(p) > 2:
        if p[2] not in variableDict:
            print("Syntax Error: VARIABLE NOT DECLARED (SHOULD BE DECLARED OUTSIDE OF BODY)")
            raise SystemExit
        p[0] = ('VAR', p[2])
    else:
        if p[1] not in variableDict:
            print("Syntax Error: VARIABLE NOT DECLARED (SHOULD BE DECLARED OUTSIDE OF BODY)")
            raise SystemExit
        p[0] = ('VAR', p[1])

    
   

    

def p_expr_constant(p):
    '''expr : cte
            | LPAREN cte RPAREN'''
    if len(p) > 2:
        p[0] = ('CTEVAL', p[2])
    else:
        p[0] = ('CTEVAL', p[1])

def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''

    p[0] = p[2]



    
# Relational expressions

def p_relexprcond(p):
    '''relexprcond : expr LT expr
               | expr GT expr
               | expr EQUALS expr
               | expr NE expr'''
    

    global quadruples
    global temps
    if(len(p[1]) == 2 and len(p[3])== 2 and isinstance(p[1], tuple) and isinstance(p[3], tuple)):
        quadruples.append([len(quadruples)+1, p[2], p[1][1], p[3][1], "t" + str(len(temps)+1)])
        #obviously this will eventually have an actual value, not just a string
        p[0] = ('CTEVAL', "t" + str(len(temps)+1))
        temps.append("val")
    elif(isinstance(p[1], str) and isinstance(p[3], str)):
        quadruples.append([len(quadruples)+1, p[2], p[1], p[3], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    elif(len(p[3])== 2 and isinstance(p[1], str)):
        quadruples.append([len(quadruples)+1, p[2], p[1], p[3][1], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    elif(len(p[1]) == 2 and isinstance(p[3], str)):
        quadruples.append([len(quadruples)+1, p[2], p[1][1], p[3], "t" + str(len(temps)+1)])
        p[0] = ("t" + str(len(temps)+1))
        temps.append("val")
    else:
        p[0] = ('RELOP', p[2], p[1], p[3])
        print(p[0])

    quadruples.append([len(quadruples)+1, "GOTOF",  "t" + str(len(temps)), "unknownloc"])
    pendinglocs.append(len(quadruples))


# Relational expressions
def p_relexprcycle(p):
    '''relexprcycle : expr LT expr
               | expr GT expr
               | expr EQUALS expr
               | expr NE expr'''
    
    global quadruples
    global temps
    global pendinglocs
    if(len(p[1]) == 2 and len(p[3])== 2):
        quadruples.append([len(quadruples)+1, p[2], p[1][1], p[3][1], "t" + str(len(temps)+1)])

        #obviously this will eventually have an actual value, not just a string
        p[0] = ('CTEVAL', "t" + str(len(temps)+1))
        temps.append("val")
    else:
        p[0] = ('RELOP', p[2], p[1], p[3])

    loc = pendinglocs.pop()
    quadruples.append([len(quadruples)+1, "GOTOT",  "t" + str(len(temps)), loc])


def p_condition(p):
    '''
    condition : IF LPAREN relexprcond RPAREN body else body SCOLON
              | IF LPAREN relexprcond RPAREN body ifend
    '''
    global quadruples
    global pendinglocs
    if len(p) == 9:
        p[0] = ("CONIFE", p[3], "GOTOT:",p[5], "GOTOF",p[7])
 
    else:
        p[0] = ("CONIF", p[3], "GOTOT:", p[5])

def p_else_mark(p):
    '''
    else : ELSE
    '''
    global quadruples
    global pendinglocs
    loc = pendinglocs.pop()-1
    quadruples[loc][3] = len(quadruples)+1

def p_ifend(p):
    '''
    ifend : SCOLON
    '''
    global quadruples
    global pendinglocs
    loc = pendinglocs.pop()-1
    quadruples[loc][3] = len(quadruples)+1


def p_cte(p):
    '''
    cte : CTEINT
        | CTEFLOAT
    '''
    p[0] = p[1]


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
    global quadruples
    global temps
    global pendinglocs
    global pendingPrints
    
    variableDict = {}
    quadruples = []
    temps = []
    pendinglocs = []
    pendingPrints = []

# Build the parser
parser = yacc.yacc()