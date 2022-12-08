def Add (a,b):
    return a+b
def substract (a,b):
    return a-b
def Multiply (a,b):
    return a*b
import math
def Mod (a,b):
    return a%b
def sqrt(a):
    return math.sqrt(a)
def division (a,b):
    return a/b
def integerdivision (a,b):
    return a//b
def expontial (a,b):
    return a**b

a=int(input())
b=int(input())
operation=int(input())
if operation==1:
    print(Add(a,b))
elif operation==2:
    print(substract(a,b))
else:
    print(Multiply(a,b))



