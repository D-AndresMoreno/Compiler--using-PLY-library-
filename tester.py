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
        X = 1 + 2;
        X = 2 + 1;
    } else {
        X = 1 / 3;
    };

    do {
        X = 4*5;
    } while(5>6);

}

end

''')

#print(test1)
#print("Variables TEST 1: ", parser_patito.variableDict)
#print("Instructions TEST 1: \n", list(parser_patito.listofinstructions.queue))
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
#print("\nVariables TEST 2: ", parser_patito.variableDict)
parser_patito.reset_variables()



#TEST 3: TESTING CYCLES

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
#print("\nVariables TEST 3: ", parser_patito.variableDict)
parser_patito.reset_variables()


#TEST 4: TESTING CONDITIONALS

test4 = parser_tester.parse('''

program PATITOS10;

var P:int; M:float;
var J:float; K:float;
{
    M = 1;

    if (5 > 0) {
         J = 1;
         M = 1;
         K = 1;
    } else {
        J = 2;
        M = 2;
        K = 2;
    };

    if(1<2){
        P = 1 + 3;
    };

    cout("hey");
}

end

''')



#print(test4)
#print("Variables TEST 4: ", parser_patito.variableDict)
#print("Instructions TEST 4: \n", list(parser_patito.listofinstructions.queue))
parser_patito.reset_variables()


#TEST 5: TESTING PRINTS

test5 = parser_tester.parse('''

program PATITOS10;

var P:int; L:float;
var A:float; M:float;
{
    cout(7, 8, 9 , 10, 11, 12);
    cout(13, 14, 15 , 16, 17, 18);
    cout(1, 2, 3);
    cout(4, 5);
    cout(P);
    cout(P + 2, (A-1)+1, "hey");
}

end

''')

#print(test5)
#print("\nVariables TEST 5: ", parser_patito.variableDict)
parser_patito.reset_variables()

