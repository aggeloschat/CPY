#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201

import sys

# ERRORS                      # To check if lex() returned ERROR, lex() <= 100 
ERROR = -100 
ERROR_UNKNOWN = -101 
ERROR_OPERATOR = -102 
ERROR_CALL_AGAIN = -103 
ERROR_BAD_DIESI = -104
ERROR_COMMENTS = - 105
ERROR_EOF = -500 
ERRORS = [ERROR,ERROR_UNKNOWN,ERROR_OPERATOR,ERROR_COMMENTS,ERROR_EOF]

# HANDLE
FOUND_ID = -1
FOUND_NUM = -2
FOUND_OPERATOR = -3
FOUND_COMMITTED = -4
FOUND_POSSIBLE_COMMITED = -5
OK = -10

COMMITTED_WORDS = ["KENO","main","def","#def","#int","global","if","elif","else","while","print","return","input","int","and","or","not"]  # To check if lex() returned commited word, lex() >= 100 and lex() < 1000
SYMBOLS = ["keno","+","-","*","//","%","<",">","==","<=",">=","!=","=",",",":","(",")","#{","#}"]                                          # To check if lex() returned symbol       , lex() >= 1000

        # 0 1 2 3  4  5  6 7  8 9 10 11 12 13 14 15 16 17              18             19        20
BOARD = [[0,1,2,OK,11,OK,3,OK,4,5,6, 7, OK,OK,OK,OK,8, ERROR_OPERATOR, ERROR_OPERATOR,ERROR_EOF,ERROR_UNKNOWN], # State 0
         [FOUND_ID,1,1,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID,FOUND_ID], # State 1 
         [FOUND_NUM,FOUND_NUM,2,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM,FOUND_NUM], # State 2
         [ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,OK,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR], # State 3 
         [FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,OK,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR], # State 4
         [FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,OK,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR], # State 5
         [FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,OK,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR], # State 6
         [ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,OK,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR], # State 7
         [ERROR_OPERATOR,12,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,ERROR_OPERATOR,9,OK,OK,ERROR_OPERATOR,ERROR_OPERATOR], # State 8
         [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,9,9,ERROR_OPERATOR,9], # State 9
         [ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_CALL_AGAIN,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS,ERROR_COMMENTS], # State 10
         [FOUND_OPERATOR,FOUND_OPERATOR,2,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR,FOUND_OPERATOR], # State 11
         [FOUND_POSSIBLE_COMMITED,12,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED,FOUND_POSSIBLE_COMMITED]  # State 12
         ]

file = None

def lex():
    verbal_unit = ""
    state = 0
    input_char = None
    input_num = None
    i = 0

    while state >= 0:    

        input_char = file.read(1)

        if input_char == "\n":
            input_num = 0
        elif input_char.isspace():          # Check for space
            input_num = 0
        elif input_char.isalpha():          # Check for letter
            input_num = 1
            if state < 3:
                i += 1
            if i == 31:
                state = FOUND_ID
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
            input_num = 19
        else:
            input_num = 20

        if (input_char != " " and input_char != "" and input_char !="\n"):
            verbal_unit += input_char

        state = BOARD[state][input_num]

    if (((state < 0) and (state > - 10) or state == ERROR_OPERATOR or state == ERROR_COMMENTS) and (input_char != " ") and (input_char != "") and (input_char !="\n")):
        file.seek(file.tell()-1)
        verbal_unit = verbal_unit[:-1]

    # HANDLING
    if state < 0 and state > -20:
        if state == FOUND_ID:
            return verbal_unit
        elif state == FOUND_OPERATOR:
            return verbal_unit
        elif state == FOUND_NUM:
            return int(verbal_unit)
        elif state == OK:
            return verbal_unit
        elif state == FOUND_POSSIBLE_COMMITED:
            if verbal_unit in COMMITTED_WORDS:
                return verbal_unit
            else:
                return str(-1*ERROR_BAD_DIESI)

    # ERRROR HANDLING
    if state < -99:
        if state == ERROR_EOF:
            return str(-1*ERROR_EOF)
        elif state == ERROR_UNKNOWN:
            return str(-1*ERROR_UNKNOWN)
        elif state == ERROR_OPERATOR:
            return str(-1*ERROR_OPERATOR)
        elif state == ERROR_COMMENTS:
            return str(-1*ERROR_COMMENTS)
        elif state == ERROR_CALL_AGAIN:
            return lex()
    


#-------------------------MAIN()-----------------------------------------------------------
file = open("test.cpy","r")

while file.read(1) != "":
    file.seek(file.tell()-1)
    id = lex()
    if isinstance(id,str):
        if id.isdigit():
            if int(id)*-1 in ERRORS:
                print(int(id)*-1)
        else:
            print(id)
    elif isinstance(id,int):
        if id >= -32767 and id <= 32767:
            print(id)
        else:
            print("Number not allowed")

"""file_name = sys.argv[1]
if (file_name[file_name.find(".")+1:]) != "cpy":
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
"""
#------------------------------------------------------------------------------------------

# OPTIONAL/RETURN IN WHICH LINE AND COLLUMN ERROR WAS FOUND
