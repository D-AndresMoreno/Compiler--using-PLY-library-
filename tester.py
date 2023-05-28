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

    K = 9 + 5;
    
    do {
        X = 4*5;
    } while(5>6);

}

end

''')


print("\nTEST 1: TESTING EVERYTHING\n")

for i in parser_patito.quadruples:
    print("\n",i)

parser_patito.reset_variables()


#TEST 2: TESTING EXPRESIONS

test2 = parser_tester.parse('''

program PATITOS10;

var P:int; L:float;
var A:float; M:float;
{
    M = 1;
    M = L;

    M = (P+1) + (2);
    M = (P/1) + (2*P);
    M = (1) + (2*P);
    M = ((P/1) + (M) / (2*P) * ((1)+2+P));

    if(1> 2){
        M = 1;
    };

    if(P > 2){
        M = 2;
    };

    if(P < M){
        M = 3;
    };

    if(((P/1) + (M) / (2*P) * ((1)+2+P)) > 1){
        M = 4;
    };

}

end

''')

print("\nTEST 2: TESTING EXPRESIONS\n")

for i in parser_patito.quadruples:
    print("\n",i)

parser_patito.reset_variables()





#TEST 3: TESTING CYCLES

test3 = parser_tester.parse('''

program PATITOS10;

var P:int; L:float;
var A:float; M:float;
{
    do {
        P = P+1;
    } while(P > M);

}

end

''')


print("\nTEST 3: TESTING CYCLES\n")

for i in parser_patito.quadruples:
    print("\n",i)

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

print("\n#TEST 4: TESTING CONDITIONALS\n")

for i in parser_patito.quadruples:
    print("\n",i)

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

print("\nTESTING PRINTS\n")

for i in parser_patito.quadruples:
    print("\n",i)

parser_patito.reset_variables()




#TEST 6: TESTING EXPRESSIONS (SMALL)

test6 = parser_tester.parse('''

program PATITOS10;

var P:int; L:float;
var A:float; M:float;
{
    A = 1+2*3/4+5;
}

end

''')

print("\nTEST 6: TESTING EXPRESSIONS (SMALL)\n")
for i in parser_patito.quadruples:
    print("\n",i)

parser_patito.reset_variables()



