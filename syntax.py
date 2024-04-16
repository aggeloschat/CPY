#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201


import sys

EOFTOKEN = 1000         # END OF FILE
ERRORTOKEN = 1001       # ERROR
CASEID = 1002           # ANAGNORISTIKO
CASECOMMITTED = 1003    # COMMITTED WORD
CASEINT = 1004          # AKERAIA STATHERA
CASEOPERATOR = 1005     # TELESTIS


# ERRORS
ERROR = -100 
ERROR_UNKNOWN = -101 
ERROR_OPERATOR = -102 
ERROR_CALL_AGAIN = -103 
ERROR_BAD_DIESI = -104
ERROR_COMMENTS = - 105
ERROR_EOF = -500 
ERRORS = [ERROR,ERROR_UNKNOWN,ERROR_OPERATOR,ERROR_COMMENTS,ERROR_EOF,ERRORTOKEN,ERROR_BAD_DIESI]

# HANDLE
FOUND_ID = -1
FOUND_NUM = -2
FOUND_OPERATOR = -3
FOUND_COMMITTED = -4
FOUND_POSSIBLE_COMMITED = -5
OK = -10

COMMITTED_WORDS = ["KENO","main","def","#def","#int","global","if","elif","else","while","print","return","input","int","and","or","not"]  # To check if lex() returned commited word, lex() >= 100 and lex() < 1000
SYMBOLS = ["KENO","+","-","*","//","%","<",">","==","<=",">=","!=","=",",",":","(",")","#{","#}"]                                         # To check if lex() returned symbol       , lex() >= 1000
OPERATORS = ["+","-","*","//","%"]
STATEMENTS = ["if","print","return","while"]

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
token_case = None
token = None

def lex():
    global token_case
    verbal_unit = ""
    state = 0
    input_char = None
    input_num = None
    i = 0

    while state >= 0 and state <= 20:    

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
                token_case = CASEID
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
            if verbal_unit in COMMITTED_WORDS:
                token_case = CASECOMMITTED
        
            else:
                token_case = CASEID
            return verbal_unit
        elif state == FOUND_OPERATOR:
            token_case = CASEOPERATOR
            return verbal_unit
        elif state == FOUND_NUM:
            token_case = CASEINT
            return int(verbal_unit)
        elif state == OK:
            token_case = CASEOPERATOR
            return verbal_unit
        elif state == FOUND_POSSIBLE_COMMITED:
            if verbal_unit in COMMITTED_WORDS:
                token_case = CASECOMMITTED
                return verbal_unit
            else:
                token_case = ERROR_BAD_DIESI
                return verbal_unit

    # ERRROR HANDLING
    if state < -99:
        token_case = ERRORTOKEN
        if state == ERROR_EOF:
            token_case = EOFTOKEN
            return verbal_unit
        elif state == ERROR_UNKNOWN:
            return verbal_unit
        elif state == ERROR_OPERATOR:
            return verbal_unit
        elif state == ERROR_COMMENTS:
            return verbal_unit
        elif state == ERROR_CALL_AGAIN:
            return lex()

#============================================================================================================================================================================================================================
#============================================================================================================================================================================================================================

#============================================================================================================================================================================================================================
#------------------------------------------------------SYNTAX--------------------------------------------------------------------------------------------------

tokens = []


#Function for creating the token list using lex()
def tokenlist():
    global tokens
    global token_case
    cur_token = lex()
    while token_case != EOFTOKEN:
        tokens.append([token_case,cur_token])
        cur_token = lex()
    tokens.append([EOFTOKEN,""])


# Class which implements the Syntax Analyzer
class Syntax:

    tokens = []

    i = 0

    def __init__(self,tokens):
        self.tokens = tokens

    # Some basic functions for handling token list

    # Next token
    def consume_next_tk(self):          
        self.i += 1

    # Peek the next token's full info
    def peek_next_tk(self):             
        return self.tokens[self.i+1]
    
    # What case is current token
    def tokencase(self):                
        return self.tokens[self.i][0]
    
    # The current token
    def tokenid(self):                  
        return self.tokens[self.i][1]

    def check_errors(self):
        if tokens[0][0] == EOFTOKEN:
            print("FILE IS EMPTY")
            exit()
        for i in tokens:
            if i[0] in ERRORS:
                print("LEX FOUND ERROR: ",i[1])
                exit()
   
   
   # Kanones tis Grammatikis mas
   
   # Kanonas tou kyriou Block tou programmatos mas
    def program(self):

        # Essential
        if self.tokencase() == CASECOMMITTED:
            # Optional
            if self.tokenid() == COMMITTED_WORDS[4]:  # "#int"
                self.consume_next_tk()
                self.declarations()
            # Optional
            if self.tokenid() == COMMITTED_WORDS[2]:  # "def"
                self.consume_next_tk()
                self.functions()
            if self.tokenid() == COMMITTED_WORDS[4]:
                print("ERROR FOUND: CAN NOT DECLARE INT AFTER DECLARING FUNCTIONS IN PROGRAM BLOCK")
                exit()
            # Essential
            if self.tokenid() == COMMITTED_WORDS[3]:  # "#def"
                self.consume_next_tk()
                self.main_part()
            else:
                print("ERROR FOUND: No Main Function found")
                exit()
        
        else:
            print("ERROR FOUND: : Found incorrect syntax in Program BLOCK")
            exit()
   
   
   
    def main_part(self):
        if self.tokenid() == COMMITTED_WORDS[1]:
            self.consume_next_tk()
            self.func_block()
            if self.tokencase() == EOFTOKEN:
                print("Compilation succesful!")
                exit()
            else:
                print("ERROR FOUND: MAIN BLOCK IS NOT IN THE END OF FILE")
                exit()
        else:
            print("Found ERROR")
            exit()    

    def declarations(self):
        self.var_list()
        if self.tokenid() == "#int":
            self.consume_next_tk()
            self.declarations()

    def var_list(self):
        if self.tokencase() == CASEID and self.peek_next_tk()[1] == ",":
            self.consume_next_tk()
            self.consume_next_tk()
            self.var_list()
        elif self.tokencase() == CASEID:
            self.consume_next_tk()
        else:
            print("FOUND ERROR")
            exit()

    def functions(self):
            if self.tokencase() == CASEID:
                self.consume_next_tk()
                if self.tokenid() == "(":
                    self.consume_next_tk()
                    self.parameters()
                    if self.tokenid() == ")":
                        self.consume_next_tk()
                        if self.tokenid() == ":":
                            self.consume_next_tk()
                            if self.tokenid() == "#{":
                                self.consume_next_tk()
                                self.func_block()
                                if self.tokenid() == "#}":
                                    self.consume_next_tk()
                                    if self.tokenid() == "def":
                                        self.consume_next_tk()
                                        self.functions()
                                        return
                                    else:
                                        return
                                
            print("ERROR FOUND: BAD SYNTAX WHILE DECLARING FUNCTION")
            exit()


    def func_block(self):
        if self.tokenid() == COMMITTED_WORDS[4]: # "#int"
            self.consume_next_tk()
            self.declarations()
        if self.tokenid() == COMMITTED_WORDS[5]: # global
            self.consume_next_tk()
            self.global_dcl()
        if self.tokenid() == COMMITTED_WORDS[4]: # "#int"
            print("ERROR FOUND: CAN NOT DECLARE INT AFTER GLOBAL IN A FUNCTION")
            exit()
        if self.tokenid() == "def":
            self.consume_next_tk()
            self.functions()
        if self.tokenid() != "#}" and self.tokencase() != EOFTOKEN:
            self.statements()

    def statements(self):
        if self.tokenid() == "def" or self.tokenid() == "#int" or self.tokenid() == "global":
            print("ERROR FOUND: CAN NOT DECLARE AFTER STATEMENTS IN A FUNCTION BLOCK")
            exit()
        self.statement()
        while self.tokenid() != "#}" and self.tokencase() != EOFTOKEN:
            self.statements()


        

    def statement(self):
        if self.tokencase() == CASEID and self.peek_next_tk()[1]  == "=":
            self.consume_next_tk()
            self.consume_next_tk()
            self.assignment()
        elif self.tokencase() == CASEID and self.peek_next_tk()[1] ==  "(":
            self.consume_next_tk()
            self.consume_next_tk()
            self.func_call()
            if self.tokenid() == ")":
                self.consume_next_tk()
            else:
                print("EXPECTED: )")
                exit()
        elif self.tokenid() in STATEMENTS:
            if self.tokenid() == "print":
                self.consume_next_tk()
                self.print_statement()
            elif self.tokenid() == "return":
                self.consume_next_tk()
                self.return_statement()


    def assignment(self):
        self.assignment_cases()

    def assignment_cases(self):
        if self.tokencase() == CASEID or self.tokencase() == CASEINT:
            self.parameters()
        elif self.tokenid() == "int":
            self.consume_next_tk()
            if self.tokenid() == "(":
                self.consume_next_tk()
                if self.tokenid() == "input":
                    self.consume_next_tk()
                    if self.consume_next_tk() == "(":
                        self.consume_next_tk()
                        if self.tokenid() == ")" and self.peek_next_tk()[1] == ")":
                            self.consume_next_tk()
                            self.consume_next_tk()
                            if self.tokenid() == ")":
                                self.consume_next_tk()
                                return

            print("ERROR FOUND: IN ASSIGNMENT SYNTAX")
            exit()

    def expressions(self):
        if self.tokencase() == CASEID and self.peek_next_tk()[1] == "(":
            self.consume_next_tk()
            self.consume_next_tk()
            self.func_call()
            if self.tokenid() == ")":
                self.consume_next_tk()
                if self.tokenid() in OPERATORS:
                    self.consume_next_tk()
                    self.expressions()
        elif (self.tokencase() == CASEINT or self.tokencase() == CASEID) and self.peek_next_tk()[1] in OPERATORS:
            self.consume_next_tk()
            self.consume_next_tk()
            self.expressions()
        elif self.tokencase() == CASEINT or self.tokencase() == CASEID:
            self.consume_next_tk()

    def parameters(self):
        self.expressions()
        if self.tokenid() == ",":
            self.consume_next_tk()
            self.parameters()

    def while_statement(self):
        return

    def if_statement(self):
        return


    def print_statement(self):
        if self.tokenid() == "(":
            self.consume_next_tk()
            self.parameters()
            if self.tokenid() == ")":
                self.consume_next_tk()
                
    def func_call(self):
        self.parameters()

    def return_statement(self):
        self.parameters()
    
    def global_dcl(self):
        self.var_list()
        if self.tokenid() == "global":
            self.consume_next_tk()
            self.global_dcl()



#====================================================Main()====================================================  

#Check if input arguments in command line are correct
if len(sys.argv) != 2:
    print("ERROR")
else:
    file_name = sys.argv[1]
    if file_name == None:
        print("ERROR")
        exit()
    elif (file_name[-4:]) != ".cpy":
        print("Wrong source file type")
        exit()
    else:
        file = open(file_name,"r")
        tokenlist() # Creating a list with id "tokens" , for better utilizing the tokens that lex() found
        parse = Syntax(tokens)
        #print(tokens)
        parse.check_errors()                                                                                                                                                                                                                                
        parse.program()
#==============================================================================================================
