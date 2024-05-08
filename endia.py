#AGGELOS KONSTANTINOS CHATZOPOULOS, 4837
#PANAGIOTIS PARIS CHATZOPOULOS, 4201

quadnum = 1 # O arithmos ths epomenhs tetradas

quadlist = []

class quad:

    global quadnum

    def __init__(self,op,x,y,z):
        
        global quadnum 
       
        self.op = op
        self.x = x
        self.y = y
        self.z = z
        self.tag = quadnum
        quadnum += 1

    def print_quad(self):

        print(self.tag,": ",self.op,",",self.x,",",self.y,",",self.z,sep='')

def nextquad():

    return quadnum

def print_quads():

    for i in range(quadnum-1):
        quadlist[i].print_quad()

quadlist = [quad("+","a",10,"y"),quad("-","b",100,"z")]

print_quads()
