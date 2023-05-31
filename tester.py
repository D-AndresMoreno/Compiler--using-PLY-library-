import parser_patito
import interpreter_patito

parser_tester = parser_patito.parser


#TEST 1: TESTING FIBONACCI

test1 = parser_tester.parse('''

program PATITOS10;

var NT1:int; NT2:int; COUNT:int; NTH:int;
var NTERMS:int;
{
    NT1 = 0;
    NT2 = 1;
    NTERMS = 500;
    COUNT = 0;

    if(NTERMS<10){
    
        cout("Ingresa un numero de NTERMS mas grande sin miedo");

    } else{
    
        do{
            
            NTH = NT1 + NT2;
        
            NT1 = NT2;
            NT2 = NTH;
            COUNT = COUNT + 1;
    
        }while(COUNT < NTERMS);

        cout(NT1);
    };
    
}

end

''')



print("\nTEST 1: CALCULO DE FIBONACCI\n")
#First parameter: bool (see quadruples or not)
#Second parameter: bool (see varsbefore or not)
#Third parameter: bool (see varsafter or not)
interpreter_patito.runProgram(False, False, False)




"""
#TEST 2: TESTING FACTORIAL

program PATITOS10;

var NUM:int; FACTORIAL:int;
var CONTADOR:int;
{
    NUM = 6;
    FACTORIAL = 1;
    CONTADOR = 1;


    do{
        FACTORIAL = FACTORIAL * CONTADOR;
        CONTADOR = CONTADOR + 1;
    }while(CONTADOR<NUM+1);

    cout("FACTORIAL ES: ", FACTORIAL);
}

end

"""