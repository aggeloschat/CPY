#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201

import sys

file_int = open("endiamesos.int",'w')
file_sym = open("table.sym",'w')

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
SYMBOLS = ["KENO","+","-","*","//","%","<",">","==","<=",">=","!=","=",",",":","(",")","#{","#}"]                                          # To check if lex() returned symbol       , lex() >= 1000
OPERATORS = ["+","-","*","//","%"]
STATEMENTS = ["if","print","return","while"]
CONDITIONS = ["<",">","==","<=",">=","!="]
CONDITIONSLOG = ["and","or","not"]

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
file_ind = 0
token_case = None
token = None

def lex():
    global token_case
    global file
    global file_ind
    verbal_unit = ""
    state = 0
    input_char = None
    input_num = None
    i = 0

    while state >= 0 and state <= 20:

        input_char = file.read(1)
        file_ind += 1

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


    if ((((state < 0) and (state > - 10)) or state == ERROR_OPERATOR or state == ERROR_COMMENTS) and (input_char != " ") and (input_char != "") and (input_char !="\n") and (input_char != "\r")):
        file_ind -= 1
        file.seek(file_ind)
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
    global file
    global tokens
    global token_case
    cur_token = lex()
    while token_case != EOFTOKEN:
        tokens.append([token_case,cur_token])
        cur_token = lex()
    tokens.append([EOFTOKEN,""])


# Class which implements the Syntax Analyzer
class Syntax:
    global file
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
        # Dimiourgoume tin tetrada gia to block tou programmatos mas
        genquad("begin_block","program","_","_")
        create_scope("program")
        if self.tokencase() == CASECOMMITTED:
            # Proeretiko
            if self.tokenid() == COMMITTED_WORDS[4]:  # "#int"
                self.consume_next_tk()
                # Lista me ta entities gia to sygkekrimeno scope
                self.declarations(VARIABLE)
            # Proeretiko
            if self.tokenid() == COMMITTED_WORDS[2]:  # "def"
                self.consume_next_tk()
                self.functions()
            if self.tokenid() == COMMITTED_WORDS[4]:  # "#int"
                print("ERROR FOUND: CAN NOT DECLARE INT AFTER DECLARING FUNCTIONS IN PROGRAM BLOCK")
                exit()
            # Ypoxreotiko
            if self.tokenid() == COMMITTED_WORDS[3]:  # "#def"
                self.consume_next_tk()
                self.main_part()
            else:
                print("ERROR FOUND: No Main Function found in the end of program")
                exit()
        else:
            print("ERROR FOUND: Bad Syntax in Main Program Block")
            exit()

    # O kanonas gia tin main sinartisi tou programmatos mas
    def main_part(self):
        if self.tokenid() == COMMITTED_WORDS[1]:
            self.consume_next_tk()
            self.func_block("mainfunc")
            # Dimiourgia tis tetradas gia ton termatismo tou programmatos mas
            genquad("halt","_","_","_")
            # Dimiourgia tis tetradas gia to telos tou block tou programmatos mas
            genquad("end_block","program","_","_")
            if self.tokencase() == EOFTOKEN:
                print("---[Compilation Successful]---")
               
                # Write ton tetradon pou dimiourgisame, sto arxeio "endiamesos.int"
                quad = firstquad
                while not quad == None:
                    quad.print_quad(file_int)
                    quad = quad.next
                
                print_table(file_sym)            
                delete_scope()
                # Exiting the syntax 
                exit()
            else:
                print("ERROR FOUND: Did not find EOF after main function")
                exit()
        else:
            print("ERROR FOUND: Expected \"main\" after \"#def\"")
            exit()

    def declarations(self,type):
        self.var_list(type)
        if self.tokenid() == "#int":
            self.consume_next_tk()
            self.declarations(VARIABLE)

    def var_list(self,type):
        if self.tokencase() == CASEID and self.peek_next_tk()[1] == ",":
            if not type == None: 
                insert_entity(self.tokenid(),VARIABLE,VALUE)
            self.consume_next_tk()
            self.consume_next_tk()
            self.var_list(type)
        elif self.tokencase() == CASEID:
            if not type == None:
                insert_entity(self.tokenid(),VARIABLE,VALUE)
            self.consume_next_tk()
        else:
            print("ERROR in var_list")
            exit()

    def functions(self):
            if self.tokencase() == CASEID:
                # Kratame sto "funcname" to onoma tis sinartisis mas
                funcname = self.tokenid()
                insert_entity(funcname,FUNC,0)
                create_scope(funcname)
                self.consume_next_tk()
                if self.tokenid() == "(":
                    self.consume_next_tk()
                    variable = [0] 
                    self.parameters(variable,0)
                    for i in range(len(variable)):
                        insert_entity(variable[i],PARAM,0)
                    if self.tokenid() == ")":
                        self.consume_next_tk()
                        if self.tokenid() == ":":
                            self.consume_next_tk()
                            if self.tokenid() == "#{":
                                # Dimiourgia tetradas gia tin arxi tou block tis sinartisis "funcname"
                                genquad("begin_block",funcname,"_","_")
                                search_entity(funcname).startQuad = nextquad()
                                self.consume_next_tk()
                                self.func_block(funcname)
                                # Dimiourgia tetradas gia to telos tou block tis sinartisis "funcname"
                                genquad("end_block",funcname,"_","_")
                                if self.tokenid() == "#}":
                                    print_table(file_sym)
                                    delete_scope()
                                    self.consume_next_tk()
                                    if self.tokenid() == "def":
                                        self.consume_next_tk()
                                        self.functions()
                                        return
                                    else:
                                        return
                                else:
                                    print("ERROR FOUND: Expected \"#}\" in the end of a function block")
                                    exit()
                            else:
                                print("ERROR FOUND: Expected \"#{\" after \":\" in the beggining of a function block")
                                exit()
                        else:
                            print("ERROR FOUND: Expected \":\" after \")\" in the declaring of a function")
                            exit()
                    else:
                        print("ERROR FOUND: Expected \")\" after \"(\" in the declaring of a function")
                        exit()
                else:
                    print("ERROR FOUND: Expected \"(\" after function id")
                    exit()
            print("ERROR FOUND: BAD SYNTAX WHILE DECLARING FUNCTION")
            exit()


    def func_block(self,funcname):
        if self.tokenid() == COMMITTED_WORDS[4]: # "#int"
            self.consume_next_tk()
            self.declarations(VARIABLE)
        if self.tokenid() == "def":
            self.consume_next_tk()
            self.functions()
        if self.tokenid() == COMMITTED_WORDS[5]: # global
            self.consume_next_tk()
            self.global_dcl()
        if self.tokenid() == "def":
            print("ERROR FOUND: CAN NOT DECLARE FUNCTION AFTER GLOBALS IN FUNCTION BLOCK")
            exit()
        if self.tokenid() == COMMITTED_WORDS[4]: # "#int"
            print("ERROR FOUND: CAN NOT DECLARE INT AFTER GLOBAL IN A FUNCTION")
            exit()
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
            tempid = self.tokenid()
            self.consume_next_tk()
            self.consume_next_tk()
            i = 0
            variable = [0]
            self.assignment(variable,i)
            genquad("=",variable[i],"_",tempid)
        elif self.tokencase() == CASEID and self.peek_next_tk()[1] ==  "(":
            funcname = self.tokenid()
            self.consume_next_tk()
            self.consume_next_tk()
            self.func_call(None,None,funcname)
            if self.tokenid() == ")":
                self.consume_next_tk()
            else:
                print("ERROR FOUND: Expected \")\" after the parameters in a function call")
                exit()
        elif self.tokenid() in STATEMENTS:
            if self.tokenid() == "print":
                self.consume_next_tk()
                self.print_statement()
            elif self.tokenid() == "return":
                self.consume_next_tk()
                self.return_statement()
            elif self.tokenid() == "if":
                self.consume_next_tk()
                exitlist = emptylist()
                self.if_statement(exitlist)
            elif self.tokenid() == "while":
                self.consume_next_tk()
                self.while_statement()
        else:
            print("ERROR FOUND:Bad syntax in statements")
            exit()


    def assignment(self,variable,i):
        self.assignment_cases(variable,i)

    def assignment_cases(self,variable,i):
        if self.tokencase() == CASEID or self.tokencase() == CASEINT:
            self.parameters(variable,0)
        elif self.tokenid() == "int":
            w = newtemp()
            insert_entity(VARIABLE,0)
            variable[i] = w
            genquad("inp",w,"_","_")
            self.consume_next_tk()
            if self.tokenid() == "(":
                self.consume_next_tk()
                if self.tokenid() == "input":
                    self.consume_next_tk()
                    if self.tokenid() == "(":
                        self.consume_next_tk()
                        if self.tokenid() == ")" and self.peek_next_tk()[1] == ")":
                            self.consume_next_tk()
                            self.consume_next_tk()
                            return
                        else:
                            print("ERROR FOUND: Expected double \")\" after parameters in input in assignment statement")
                            exit()
                    else:
                        print("ERROR FOUND: Expected \"(\" after \"input\" in assignment statement")
                        exit()
                else:
                    print("ERROR FOUND: Expected \"input\" after \"(\" in assignment statement")
                    exit()
            else:
                print("ERROR FOUND: Expected \"(\" after \"int\" in assignment statement")
                exit()
        else:
            print("ERROR FOUND: Bad syntax in assignment")
            exit()

    def expressions(self,variable,i):
        found_not = 0
        if self.tokenid() == "not":
            found_not += 1
            self.consume_next_tk()

        if self.tokencase() == CASEID and self.peek_next_tk()[1] == "(":
            funcname = self.tokenid()
            self.consume_next_tk()
            self.consume_next_tk()
            nestedvariable = [0] # For the temp value that will be returned from the function call
            self.func_call(nestedvariable,0,funcname)
            if not variable == None:
                variable[i] = nestedvariable[0]
            if self.tokenid() == ")":
                self.consume_next_tk()
                if self.tokenid() in OPERATORS:
                    tempoperator = self.tokenid()
                    self.consume_next_tk()
                    variable1 = [0]
                    w = newtemp()
                    insert_entity(w,VARIABLE,0)
                    self.expressions(variable1,0)
                    genquad(tempoperator,variable[i],variable1[0],w)
                    if not variable == None:
                        variable[i] = w
                elif self.tokencase() == CASEINT and self.tokenid() < 0:
                    self.expressions()
        elif (self.tokencase() == CASEINT or self.tokencase() == CASEID) and self.peek_next_tk()[0] == CASEINT and self.peek_next_tk()[1] < 0:
            tempnum1 = self.tokenid()
            tempnum1case = self.tokencase()
            self.consume_next_tk()
            tempnum2 = self.tokenid()
            self.consume_next_tk()
            self.tokens.insert(self.i,[CASEINT,(abs(tempnum2))])
            self.tokens.insert(self.i,[CASEOPERATOR,"-"])
            self.tokens.insert(self.i,[tempnum1case,tempnum1])
            self.expressions(variable,i)
        elif (self.tokencase() == CASEINT or self.tokencase() == CASEID) and self.peek_next_tk()[1] in OPERATORS:
            tempid = self.tokenid()
            self.consume_next_tk()
            tempoperator = self.tokenid()
            self.consume_next_tk()
            w = newtemp()
            insert_entity(w,VARIABLE,0)
            variable1 = [0]
            self.expressions(variable1,0)
            genquad(tempoperator,tempid,variable1[0],w)
            if not variable == None: 
                variable[i] = w
        elif self.tokencase() == CASEINT or self.tokencase() == CASEID:
            tempid = self.tokenid()
            self.consume_next_tk()
            if not variable == None:
                    variable[i] = tempid

    def parameters(self,variable,i):
        self.expressions(variable,i)
        if self.tokenid() == ",":
            self.consume_next_tk()
            if not variable == None:
                variable.append(0)
                self.parameters(variable,i+1)
            else:
                self.parameters(None,None)

    def while_statement(self):
        while_tag= nextquad()
        variable = [0]
        c = kanonas(emptylist(),emptylist())
        self.condition(variable,0,c)
        if self.tokenid() == ":":
            self.consume_next_tk()
            if self.tokenid() == "#{":
                self.consume_next_tk()
                while self.tokenid() != "#}":
                    self.statement()
                if self.tokenid() == "#}":
                    backpatch(c.ltrue,nextquad())
                    genquad("jump","_","_",while_tag)
                    backpatch(c.lfalse,nextquad())
                    self.consume_next_tk()
                    return
                else:
                    print("ERROR FOUND: Expected \"#}\" in the end of \"while\" block")
                    exit()
            else:
                print("ERROR FOUND: Expected \"#{\" in the start of \"while\" block")
                exit()

    def if_statement(self,exitlist):
        if self.tokencase() != CASEID and self.tokencase() != CASEINT and self.tokenid() != "not":
            print("ERROR FOUND: Bad syntax in condition in \"if\" statement")
            exit()
        variable = [0]
        c = kanonas(emptylist(),emptylist())
        self.condition(variable,0,c)
        if self.tokenid() == ":":
            self.consume_next_tk()
            self.statement()
            if self.tokenid() == "elif":
                variable1 = [0]
                self.else_statement(variable,0,c,exitlist)
                if not self.tokenid() == "else":
                    print("ERROR FOUND: After \"elif\" 's block expected \"else\"")
                    exit()
            if self.tokenid() == "else":
                exitlist.append(nextquad())
                genquad("jump","_","_","_",)
                backpatch(c.lfalse,nextquad())
                self.consume_next_tk()
                if self.tokenid() == ":":
                    self.consume_next_tk()
                    self.statement()
                    backpatch(exitlist,nextquad())
                    return
                else:
                    print("ERROR FOUND: Expected \" after \"else\" in if statement")
                    exit()
            else:
                backpatch(exitlist,nextquad())
                backpatch(c.ltrue,nextquad())
                backpatch(c.lfalse,nextquad())
                return
        print("ERROR IN IF STATEMENT")
        exit()

    def else_statement(self,variable,i,c,exitlist):
            if self.tokenid() == "elif":
                exitlist.append(nextquad())
                genquad("jump","_","_","_")
                backpatch(c.lfalse,nextquad())
                self.consume_next_tk()
                self.condition(variable,i,c)
                if self.tokenid() == ":":
                    self.consume_next_tk()
                    self.statement()
                    self.else_statement(variable,i,c,exitlist)
                else:
                    print("ERROR FOUND: In \"elif\" statement expected \":\"")
                    exit(0)

    def condition(self,variable,i,c):
        found_not = 0
        if self.tokenid() == "not":
            found_not = 1
            self.consume_next_tk()
        self.expressions(variable,i)
        if self.tokenid() in CONDITIONS:
            tempcondition = self.tokenid()
            self.consume_next_tk()
            variable1 = [0]
            j = 0
            self.expressions(variable1,0)
            c.ltrue.append(nextquad())
            genquad(tempcondition,variable[i],variable1[j],"_")
            c.lfalse.append(nextquad())
            genquad("jump","_","_","_")
            if found_not == 1:
                temp_list = c.lfalse
                c.lfalse = c.ltrue
                c.ltrue = temp_list
            if self.tokenid() in CONDITIONSLOG:
                if self.tokenid() == "or":
                    self.consume_next_tk()
                    variable.append(0)
                    
                    backpatch(c.lfalse,nextquad())
                    self.condition(variable,i+1,c)
                elif self.tokenid() == "and":
                    self.consume_next_tk()
                    variable.append(0)
                    backpatch(c.ltrue,nextquad()) 
                    self.condition(variable,i+1,c)
            
            backpatch(c.ltrue,nextquad())
            return
        else:
            print("ERROR FOUND: Expected operator in condition in \"if\" and \"elif\"statements")
            exit()

    def print_statement(self):
        if self.tokenid() == "(":
            self.consume_next_tk()
            variable = [0]
            i = 0
            self.parameters(variable,i)
            if self.tokenid() == ")":
                self.consume_next_tk()
                genquad("out",variable[i],"_","_")
            else:
                print("ERROR FOUND: AFTER PRINT PARAMETERS EXPECTED \")\"")
                exit()
        else:
            print("ERROR FOUND: AFTER PRINT EXPECTED: \"(\"")
            exit()

    def func_call(self,variable,i,funcname):
            return_needed = 0 
            if variable == None:
                variable = [0] 
                i = 0
            else:
                return_needed = 1
            self.parameters(variable,i)
            j = i
            for z in range(len(variable)):
                if variable[j] != 0:
                    genquad("par",variable[j],"CV","_")
                j += 1
            w = newtemp()
            insert_entity(w,VARIABLE,0)
            if return_needed:
                genquad("par",w,"RET","_")
            genquad("call","_","_",funcname)
            variable[i] = w
 
    def return_statement(self):
        variable = [0]
        self.parameters(variable,0)
        genquad("retv",variable[0],"_","_")

    def global_dcl(self):
        self.var_list(None)
        if self.tokenid() == "global":
            self.consume_next_tk()
            self.global_dcl()

#=============================================================ENDIA=================================================================================
#===================================================================================================================================================

quadnum = 1 # O arithmos ths epomenhs tetradas

# H domi/klasi gia tis tetrades
class quad:

    next = None

    def __init__(self,op,x,y,z):
        
        self.op = op
        self.x = x
        self.y = y
        self.z = z
        self.tag = quadnum

    def print_quad(self,file):

        print(self.tag,": ",self.op,",",self.x,",",self.y,",",self.z,sep='',file=file)

class kanonas:

    ltrue = []
    lfalse = []
    
    def __init__(self,ltrue,lfalse):

        self.ltrue = ltrue
        self.lfalse = lfalse

# Voithikes yporoutines

# H prwth tetrada pou tha dimiourgithei
firstquad = None

def genquad(op,x,y,z):
    global firstquad
    global quadnum

    if quadnum == 1:
        firstquad = quad(op,x,y,z)
        quadnum += 1
    elif quadnum == 2:
        firstquad.next = quad(op,x,y,z)
        quadnum += 1
    else:
        tempquad = firstquad
        while not tempquad.next == None:
            tempquad = tempquad.next
        tempquad.next = quad(op,x,y,z)
        quadnum += 1

def nextquad():

    return quadnum

def print_quads():

    for i in range(quadnum-1):
        quadlist[i].print_quad()

tempcount = 1

def newtemp():

    global tempcount

    tempcreated = "T_"+str(tempcount)
    tempcount += 1

    return tempcreated

def emptylist():

    return []

def makelist(x):
   
    return [x]

def mergelist(list1,list2):

    j = len(list1)
    templist = list1.copy()
    for i in range(len(list2)):
        templist.append(list2[i])
    return templist

def backpatch(list,z):
    
    tempquad = firstquad
    while not tempquad == None:
        if tempquad.tag in list:
            if tempquad.z == "_":
                tempquad.z = z 
        tempquad = tempquad.next

def print_quads():
    tempquad = firstquad

    while not tempquad == None:

        tempquad.print_quad()
        tempquad = tempquad.next

"""
genquad("+","a","b","c")
genquad("<=","xx","tetst","200")
genquad(":=","sdfads","tdssdf","200")
l1=makelist(nextquad())
genquad(">","x","a","_")
l2=makelist(nextquad())
genquad("jump","_","_","_")
l1=mergelist(l1,l2)
backpatch(l1,nextquad())
print_quads()
"""


#===================================================TABLE======================================================
#==============================================================================================================

PARAM = 0
FUNC = 1
VARIABLE = 2

VALUE = 100

class entity:

    name = None
    type = None             # Parametros,Sinartisi,Metavliti
    offset = None           # Gia tis metavlites kai parametrous
    parammode = None        # Gia parametro an einai call by value
    nestinglevel = None     # Vathos foliasmatos gia tis metavlites (local/global)
    
    startQuad = None       # Gia tis sinartisis
    argument = None        # Lista parametron 
    framelength = None     # Mikos egrafimatos drastiriopiisis
    
    next = None             # Gia tin lista
    

class scope:

    name = None
    nestinglevel = None     # vathos foliasmatos
    elist = None            # Lista me ta entities gia to sygkekrimeno scope
    next = None
    

SCOPES = None # Head of the stack

def create_scope(name):

    global SCOPES
    new_scope = scope()
    new_scope.name = name

    if SCOPES == None:
        SCOPES = new_scope
        new_scope.nestinglevel = 0
        new_scope.next = None
    else:
        new_scope.nestinglevel = SCOPES.nestinglevel + 1
        new_scope.next = SCOPES
        SCOPES = new_scope

def delete_scope():
    global SCOPES

    if SCOPES == None:
        print("There is no scope to delete")
        exit()

    else:
        SCOPES = SCOPES.next


def insert_entity(name,type,parammode):

    global SCOPES

    new_entity = entity()
    new_entity.name = name
    new_entity.type = type
    new_entity.parammode = parammode
    new_entity.nestinglevel = SCOPES.nestinglevel


    prev = None
    tmp = SCOPES.elist
    while not tmp == None:
        prev = tmp
        if not tmp.type == FUNC:
            lastoffset = tmp.offset
        tmp=tmp.next
    if prev == None:
        SCOPES.elist = new_entity
        new_entity.offset = 12
    else:
        prev.next = new_entity
        new_entity.offset = lastoffset + 4

def search_entity(name):
    global SCOPES
    tmp_entity = None
    tmp_scope = None

    tmp_scope = SCOPES
    while not tmp_scope == None:
        tmp_entity = tmp_scope.elist
        while not tmp_entity == None: 
            if tmp_entity.name == name:
                return tmp_entity
            tmp_entity = tmp_entity.next
        tmp_scope = tmp_scope.next
    return None

print_num = 1

def print_table(file):
    global SCOPES
    global print_num
    
    tmp_entity = None
    tmp_scope = None
    
    print("[ PRINT",print_num,"]",file=file)
    print_num += 1
    print("============================================================================\n",file=file)
    tmp_scope = SCOPES
    while not tmp_scope == None:
        tmp_entity = tmp_scope.elist
        print("SCOPE:",tmp_scope.name,file=file)
        while not tmp_entity == None:
            if tmp_entity.type == VARIABLE:
                print(tmp_entity.name,"/",tmp_entity.offset,file=file)
            elif tmp_entity.type == PARAM:
                print(tmp_entity.name,"/",tmp_entity.offset,"/","CV",file=file)
            elif tmp_entity.type == FUNC:
                print(tmp_entity.name,"/",tmp_entity.framelength,"/",tmp_entity.startQuad,file=file)
            else:
                print(tmp_entity.name,file=file)
            tmp_entity = tmp_entity.next
        print(file=file)
        tmp_scope = tmp_scope.next




"""create_scope("main")
insert_entity("x",VARIABLE,0)
insert_entity("y",VARIABLE,0)
insert_entity("myfunction",FUNC,0)
create_scope("myfunction")
insert_entity("i",VARIABLE,0)
insert_entity("j",VARIABLE,0)
print_table()"""


#====================================================Main()====================================================  
#============================================================================================================== 

#Check if input arguments in command line are correct
if len(sys.argv) != 2:
    print("ERROR WHEN CALLING SYNTAX")
else:
    file_name = sys.argv[1]
    if file_name == None:
        print("ERROR")
        exit()
    elif (file_name[-4:]) != ".cpy":
        print("Wrong source file type")
        exit()
    else:
        file = open(file_name,"r+")
        tokenlist()       # Creating a list with id "tokens" , for better utilizing the tokens that lex() found
        parse = Syntax(tokens)
        #print(tokens)  
        parse.check_errors()
        parse.program()

#==============================================================================================================
#============================================================================================================== 
