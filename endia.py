#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201

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

    def print_quad(self):

        print(self.tag,": ",self.op,",",self.x,",",self.y,",",self.z,sep='')

class kanonas:

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
