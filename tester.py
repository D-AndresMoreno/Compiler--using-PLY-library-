from ply import *
import lexer_patito
import parser_patito

lexer_patito = Lexer().get()
parser = Parser().parse()

tokens = lexer_patito.lex("""

program PATITOS;

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

}end

""")
                   
parser.parse(tokens)