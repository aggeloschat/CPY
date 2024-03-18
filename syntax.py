#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201

import sys

# ERRORS <= -100
ERROR = -100 # Found Error
ERROR_UNKNOWN = -101 # Character not allowed
ERROR_COMMENTS = -102

# HANDLES < 0
EOF = 19  # End Of File
BACK = -3 # Return last character and go back one step
CALL_AGAIN = -4 
EOVU = -12  # End Of verbal unit

FOUND_NUMBER = -11     # Akeraia stathera
FOUND_COMMITED =-12    # Desmeumeni leksi
FOUND_OPERATOR = -13    # Telestis/symbolo
FOUND_IDENTIFIER = -14 # Anagnoristiko

# COMMITED WORDS >= 100
MAIN = 100
DEF = 200
DIESIDEF = 300
DIESIINT = 400
GLOBAL = 500
EAN = 600
ALLIOSEAN = 700
ALLIOS = 800
OSO = 900
TYPOSE = 1000
EPESTREPSE = 1100
EISODOS = 1200
AKERAIOS = 1300
KAI = 1400
DIAZEUKSI = 1500
ARNISI = 1600

COMMITED_WORDS = ["KENO","main","def","#def","#int","global","if","elif","else","while","print","return","input","int","and","or","not"]

file = None       # Deikths sto source file


def lex():
    verbal_unit = ""    #Lektikh Monada
    state = 0           # H katastash pou briskomaste sto automato
    input_char = None
    input_num = None
    i = 0
    line = 1
    collumn = 0

    while state >= 0 and state <= 18:

        input_char = file.read(1)
        if input_char == "\n":
            line += 1
            input_num = 0
            collumn -= 1
        elif input_char.isspace():          # Check for space
            input_num = 0
        elif input_char.isalpha():          # Check for letter
            input_num = 1
            i += 1
            if i == 31:
                state = FOUND_IDENTIFIER
                return verbal_unit
        elif input_char.isdigit():          # Check for number
            input_num = 2
        elif input_char == "+":
            input_num = 3
        elif input_char == "-":
            input_num = 4
        elif input_char == "*":
            input_num = 5
        elif input_char == "/":
            input_num = 6
        elif input_char == "%":
            input_num = 7
        elif input_char == "<":
            input_num = 8
        elif input_char == ">":
            input_num = 9
        elif input_char == "=":
            input_num = 10
        elif input_char == "!":
            input_num = 11
        elif input_char == ",":
            input_num = 12
        elif input_char == ":":
            input_num = 13
        elif input_char == "(":
            input_num = 14
        elif input_char == ")":
            input_num = 15
        elif input_char == "#":
            input_num = 16
        elif input_char == "{":
            input_num = 17
        elif input_char == "}":
            input_num = 18
        elif input_char == "":
            input_num = EOF
        else:
            input_num = 20
        verbal_unit += input_char
        collumn += 1
        state = board[state][input_num]
    


    # HANDLING ERROR
    if state <=  -100:
        if state == ERROR_UNKNOWN:
           print("Invalid character found in Line :", line," Collumn:",collumn)
           return ERROR_UNKNOWN
        elif state == ERROR_COMMENTS:
            print("Comments not closed")
            return ERROR_COMMENTS
        return ERROR_UNKNOWN
    #-----------------------------

    if state == BACK:
        file.seek(file.tell()-1)
        verbal_unit = verbal_unit[:-1]
        return verbal_unit
    elif state == CALL_AGAIN:
        return lex()
    elif state == EOF:
        return 19
    else:
        if state == FOUND_NUMBER:
            return int(verbal_unit)
        elif state == FOUND_IDENTIFIER:
            if verbal_unit in COMMITED_WORDS:
                return COMMITED_WORDS.index(verbal_unit)*100
            else:
                return verbal_unit
        elif state == FOUND_OPERATOR:
            return verbal_unit

board = [[0,1,2,FOUND_OPERATOR,11,FOUND_OPERATOR,3,FOUND_OPERATOR,4,5,6,7,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,8,0,ERROR,EOF,ERROR_UNKNOWN], # State 0
         [FOUND_IDENTIFIER,1,1,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_IDENTIFIER,ERROR_UNKNOWN], # State 1
         [FOUND_NUMBER,FOUND_NUMBER,2,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER,FOUND_NUMBER], # State 2
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,FOUND_OPERATOR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR], # State 3
         [BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,FOUND_OPERATOR,BACK], # State 4 
         [BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,FOUND_OPERATOR,BACK], # State 5
         [BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,BACK], # State 6
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,FOUND_OPERATOR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,FOUND_OPERATOR,BACK], # State 7
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,FOUND_OPERATOR,ERROR,ERROR,ERROR,ERROR,ERROR,9,FOUND_OPERATOR,FOUND_OPERATOR,ERROR,ERROR,ERROR], # State 8
         [9,9,9,9,9,9,9,9,9,9,10,9,9,9,9,9,10,9,9,ERROR_COMMENTS,9], # State 9
         [ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,CALL_AGAIN,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS], # State 10
         [BACK,BACK,2,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,FOUND_OPERATOR,FOUND_OPERATOR], # State 11
         ]


#        DELETE BEFORE FINISHED
file = open("test.txt","r")
if file.read().isspace():    # In case file is empty
    print("File is empty")  
else:
    file.seek(0)
    
    while file.read(1) != "":
        file.seek(file.tell()-1 )
        print(lex())

"""
#-----------------------------------------------------------------
#---------------------------MAIN()--------------------------------
file_name = sys.argv[1]
if (file_name[file_name.find(".")+1:]) != "py":
    print("Wrong source file type")
    exit()
else:
    file = open(file_name,"r")
    if file.read().isspace():    # In case file is empty
            print("File is empty")  
    else:
        file.seek(0)
    
        while file.read(1) != "":
            file.seek(file.tell()-1 )
            print(lex())
#-----------------------------------------------------------------
#-----------------------------------------------------------------
"""
