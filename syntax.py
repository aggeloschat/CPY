#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201

# file.seek(file.tell()-1) // Gia na paw ena bima piso sto file

import sys

EOVU = -3  # End Of verbal unit
ERROR = -1 # Found Error
EOF = -2   # End Of File
BACK = -4  # Return last character and go back one step

#lex.file = open(sys.argv[1],"r") # Anoigma tou source file ston lex
file = open("test.txt","r")       # Diagrafh sto telos ton testing kai anoigma tou apo panw


def lex():
    verbal_unit = ""    #Lektikh Monada
    state = 0           # H katastash pou briskomaste sto automato
    input_char = None
    input_num = None

    while (state >= 0) and (state <= 100):
        input_char = file.read(1)

        if input_char.isspace():          # Check for space
            input_num = 0
            input_char = ""
        elif input_char.isalpha():        # Check for letter
            input_num = 1
        elif input_char.isdigit():        # Check for number
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
            input_num = 0
            print("File ended")
        else:
            input_num = 20
            print("ERROR")
        verbal_unit += input_char
        state = board[state][input_num]
    
    if state == BACK:
        file.seek(file.tell()-1)
        verbal_unit = verbal_unit[:-1]
        return verbal_unit
    elif state == ERROR:
        print("Error found")
        return ""
    elif state == EOF:
        print("ERROR EOF")
        return ""
    else:
        return verbal_unit

board = [[0,1,2,EOVU,EOVU,EOVU,3,EOVU,4,5,6,7,EOVU,EOVU,EOVU,EOVU,8,0,EOF,ERROR], # State 0
         [EOVU,1,1,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOF,ERROR], # State 1
         [EOVU,EOVU,2,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOVU,EOF,ERROR], # State 2
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,EOVU,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR], # State 3
         [BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,EOVU,BACK,BACK,BACK,BACK,BACK,BACK,BACK,EOF,ERROR], # State 4
         [BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,EOVU,BACK,BACK,BACK,BACK,BACK,BACK,BACK,EOF,ERROR], # State 5
         [BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,BACK,EOVU,BACK,BACK,BACK,BACK,BACK,BACK,BACK,EOF,ERROR], # State 6
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,EOVU,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR], # State 7
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,EOVU,ERROR,ERROR,ERROR,ERROR,ERROR,9,EOVU,EOVU,ERROR], # State 8
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,EOVU,ERROR,ERROR,ERROR,ERROR,ERROR,10,ERROR,ERROR,ERROR], # State 9
         [ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,EOVU,ERROR,ERROR,ERROR,ERROR,ERROR,0,ERROR,ERROR,ERROR], # State 10
         ]

while file.read(1) != "":
    file.seek(file.tell()-1 )
    print(lex())