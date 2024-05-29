
outputFile = open("telikos.asm","w")

class final:

    outputFile = None

    ent = search_entity(v);

    def __init__(self,fileEndia):
        self.outputFile = outputFile

    def loadvr(self,v,r):
        
        # An v einai stathera
        if str(v).isdigit():
            print("li t"+str(r)+", v",file=outputFile)
        # An v einai global
        elif ent.nestinglevel == 0:
            print("lw t"+str(r)+", -"+ent.offset+"(gp)",file=outputFile)

temp = final(outputFile)

temp.loadvr(2,3)

