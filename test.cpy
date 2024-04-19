#int counterFunctionCalls

def max3(x,y,z):
#{
    #int m
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    if x>y:
        m = x
    elif y>x:
        m = y
    else:
        m = z
    return m
#}


def fib(x):
#{
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    if x<0:
        return -1
    elif x==1:
        return 1
    else:
        return a
#}
     
     
def isPrime(x):
#{
    #int i

    def divides(x,y):
    #{
        global counterFunctionCalls
        counterFunctionCalls = counterFunctionCalls + 1
        if y == a:
            return 1
        else:
            return 0
    #}
    counterFunctionCalls = counterFunctionCalls + 1
    i = 2
    return 1
#}

     
def quad(x):
#{
    #int y

    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    y = sqr(x)*sqr(x)
    return y
#}


def leap(year):
#{
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    if year%4==0:
        return 1
    else:
        return 0 
#}        


        
#def main
#int i
counterFunctionCalls = 0

i = int(input())
print(i)


i = 1600
while i<=2000:

print(leap(2023))
print(leap(2024))
print(quad(3))
print(fib(5))

i=1


print(counterFunctionCalls)

