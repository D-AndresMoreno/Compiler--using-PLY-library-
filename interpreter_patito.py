import parser_patito
from queue import Queue

parser_tester = parser_patito.parser

quadruples = parser_patito.quadruples


eof = False
count = 0

temps = parser_patito.temps
quadruples  = parser_patito.quadruples
variabledict = parser_patito.variableDict
pendingPrints = parser_patito.pendingPrints
pendingPrints.reverse()


def checkVarValue(var):
    #print("A ver",var)
    if var in variabledict:
        
        if(variabledict[var][1] == None):
            print("Variable needs to be assigned a value before using it")
            raise SystemExit
        
        if(variabledict[var][0] == "float"):
            return float(variabledict[var][1])
        if(variabledict[var][0] == "int"):
            return int(variabledict[var][1])
    else:
        if(var[:1] == 't'):
            return temps[int(var[1:])-1]
        

        #print("Variable doesnt exist in dictionary")
        return -1

def isDigitOrFloat(x):
    if(x.isdigit()):
        return True
    elif(isinstance(x, str)):
        try:
            float(x)
            return True
        except ValueError:
            return False
    else:
        print("Wtf is this: ", type(x))
        return False
        
def runProgram(v_quadruples, varsbefore, varsafter):
    eof = False
    count = 0
    temps = parser_patito.temps
    quadruples  = parser_patito.quadruples
    variabledict = parser_patito.variableDict
    
    if(varsbefore):
        print("After: ", variabledict)
    while(not eof):
        if(v_quadruples):
            print(quadruples[count])

        if(quadruples[count][1] == '+'):
            indexoftemp = int(quadruples[count][4][1:])-1
            #print("Index :", indexoftemp)
            if(isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                temps[indexoftemp] = float(quadruples[count][2]) + float(quadruples[count][3]) 
            elif(not isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3]) ):
                val1 = checkVarValue(quadruples[count][2])
                temps[indexoftemp] = val1 + float(quadruples[count][3]) 
            elif(isDigitOrFloat(quadruples[count][2]) and not isDigitOrFloat(quadruples[count][3])):
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = float(quadruples[count][2]) + val2
                #print(float(quadruples[count][2]), val2)
            else:
                #las dos son variables 
                val1 = checkVarValue(quadruples[count][2])
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = val1 + val2

        elif(quadruples[count][1] == '-'):
            indexoftemp = int(quadruples[count][4][1:])-1
            #print("Index :", indexoftemp)
            if(isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                temps[indexoftemp] = float(quadruples[count][2]) - float(quadruples[count][3]) 
            elif(not isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                val1 = checkVarValue(quadruples[count][2])
                temps[indexoftemp] = val1 - float(quadruples[count][3]) 
            elif(isDigitOrFloat(quadruples[count][2]) and not isDigitOrFloat(quadruples[count][3])):
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = float(quadruples[count][2]) - val2
            else:
                val1 = checkVarValue(quadruples[count][2])
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = val1 - val2
        
        elif(quadruples[count][1] == '*'):
            indexoftemp = int(quadruples[count][4][1:])-1
            #print("Index :", indexoftemp)
            if(isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                temps[indexoftemp] = float(quadruples[count][2]) * float(quadruples[count][3]) 
            elif(not isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                val1 = checkVarValue(quadruples[count][2])
                temps[indexoftemp] = val1 * float(quadruples[count][3]) 
            elif(isDigitOrFloat(quadruples[count][2]) and not isDigitOrFloat(quadruples[count][3])):
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = float(quadruples[count][2]) * val2
            else:
                val1 = checkVarValue(quadruples[count][2])
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = val1 * val2

        
        elif(quadruples[count][1] == '/'):
            indexoftemp = int(quadruples[count][4][1:])-1
            #print("Index :", indexoftemp)
            if(isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                temps[indexoftemp] = float(quadruples[count][2]) / float(quadruples[count][3]) 
            elif(not isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                val1 = checkVarValue(quadruples[count][2])
                temps[indexoftemp] = val1 / float(quadruples[count][3]) 
            elif(isDigitOrFloat(quadruples[count][2]) and not isDigitOrFloat(quadruples[count][3])):
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = float(quadruples[count][2]) / val2
            else:
                val1 = checkVarValue(quadruples[count][2])
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = val1 + val2

        elif(quadruples[count][1] == '='):
            typeof = variabledict[quadruples[count][2]][0]
            if(isDigitOrFloat(quadruples[count][3])):
                if(isDigitOrFloat(quadruples[count][3])):
                    typeof = 'int'
                else:
                    typeof = 'float'
                variabledict[quadruples[count][2]] = (typeof, quadruples[count][3])
            elif checkVarValue((quadruples[count][3])) != -1 and quadruples[count][3][:1] != 't':
                variabledict[quadruples[count][2]] = (typeof, variabledict[quadruples[count][3]][1])
            else:
                #print("wTF:", int(quadruples[count][3][1:])-1)
                indexoftemp = int(quadruples[count][3][1:])-1       
                variabledict[quadruples[count][2]] = (typeof, temps[indexoftemp])
        
        elif(quadruples[count][1] == '>'):
            indexoftemp = int(quadruples[count][4][1:])-1
            #print("Index :", indexoftemp)
            if(isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                temps[indexoftemp] = float(quadruples[count][2]) > float(quadruples[count][3]) 
            elif(not isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                val1 = checkVarValue(quadruples[count][2])
                #print("Si es aqui")
                temps[indexoftemp] = val1 > float(quadruples[count][3]) 
            elif(isDigitOrFloat(quadruples[count][2]) and not isDigitOrFloat(quadruples[count][3])):
                val2 = checkVarValue(quadruples[count][3])
                #print("Si es aca")
                temps[indexoftemp] = float(quadruples[count][2]) > val2
            else:
                val1 = checkVarValue(quadruples[count][2])
                val2 = checkVarValue(quadruples[count][3])
                #print("Entonces hasta aca?", val1, val2)
                temps[indexoftemp] = val1 > val2

        elif(quadruples[count][1] == '<'):
            indexoftemp = int(quadruples[count][4][1:])-1
            #print("Index :", indexoftemp)
            if(isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                temps[indexoftemp] = float(quadruples[count][2]) < float(quadruples[count][3]) 
            elif(not isDigitOrFloat(quadruples[count][2]) and isDigitOrFloat(quadruples[count][3])):
                val1 = checkVarValue(quadruples[count][2])
                temps[indexoftemp] = val1 < float(quadruples[count][3]) 
            elif(isDigitOrFloat(quadruples[count][2]) and not isDigitOrFloat(quadruples[count][3])):
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = float(quadruples[count][2]) < val2
            else:
                val1 = checkVarValue(quadruples[count][2])
                val2 = checkVarValue(quadruples[count][3])
                temps[indexoftemp] = val1 < val2
                #print("Entonces hasta aca2?", val1, val2)
                #las dos son variables 
        
        elif(quadruples[count][1] == 'GOTO'):
            ## Le restamos 2 al final porque los cuadruplos empiezan desde 1 (no 0), y para el contador de al final del while
            count  = int(quadruples[count][2]) - 2

        elif(quadruples[count][1] == 'GOTOF'):
            indexoftemp = int(quadruples[count][2][1:])-1
            if(not temps[indexoftemp]):
                ## Le restamos 2 al final porque los cuadruplos empiezan desde 1 (no 0), y para el contador de al final del while
                count  = int(quadruples[count][3]) - 2

        elif(quadruples[count][1] == 'GOTOT'):
            indexoftemp = int(quadruples[count][2][1:])-1
            if(temps[indexoftemp]):
                ## Le restamos 2 al final porque los cuadruplos empiezan desde 1 (no 0), y para el contador de al final del while
                count  = int(quadruples[count][3]) - 2

        elif(quadruples[count][1] == 'PRINT'):

            prints  =  quadruples[count][2]
            #print(quadruples[count])

            if(isDigitOrFloat(prints)):
                print(prints)
            elif(isinstance(prints, str)):
                if(checkVarValue(prints) == -1):
                    #print("Yo soy el culpable: ", prints)
                    print(prints)
                else:
                    print(variabledict[prints][1])

        elif(quadruples[count][1] == "END"):
            eof = True

        else:
            print("Unrecognized token: ", quadruples[count][1])
        count += 1
    if(varsafter):
        print("After: ", variabledict)
    parser_patito.reset_variables()
