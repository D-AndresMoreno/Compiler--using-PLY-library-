import parser_patito
import lexer_patito

parser_tester = parser_patito.parser


#TEST 1: TESTING EVERYTHING

test1 = parser_tester.parse('''

program PATITOS10;

var X:int; Z:float;
var J:float; K:float;
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

#print(test1)
print("Variables TEST 1: ", parser_patito.variableDict)
parser_patito.reset_variables()


#TEST 2: TESTING EXPRESIONS

test2 = parser_tester.parse('''

program PATITOS10;

var P:int; L:float;
var A:float; M:float;
{
    M = 1;
    M = L;

    M=1+1;
    M=2-1;
    M=2*1;
    M=2/1;

    M=P+1;
    M=P-1;
    M=P*1;
    M=P/1;

    M=1+P;
    M=1-P;
    M=1*P;
    M=1/P;

    M=P+P;
    M=P-P;
    M=P*P;
    M=P/P;

    M = (P+1) + (2);
    M = (P/1) + (2*P);
    M = (1) + (2*P);
    M = ((P/1) + (M) / (2*P) * ((1)+2+P));

    if(1> 2){
    
    };

    if(P > 2){
    
    };

    if(P < M){
    
    };

    if(((P/1) + (M) / (2*P) * ((1)+2+P)) > 1){
    
    };

}

end

''')

#print(test2)
print("\nVariables TEST 2: ", parser_patito.variableDict)
parser_patito.reset_variables()



#TEST 3: TESTING CYCLES AND PRINTS

test3 = parser_tester.parse('''

program PATITOS10;

var P:int; L:float;
var A:float; M:float;
{
    do {
         cout(P, "hey", 1+1, (P+P*1));
    } while(A > M);

    cout(A>L, 8);

}

end

''')

#print(test3)
print("\nVariables TEST 3: ", parser_patito.variableDict)
parser_patito.reset_variables()
