from functools import reduce
arr1=[19,20,7,3,5,10,12,18,21,31,51,29]
def checkprime(n):
    for i in range(2,n):
        if n%i ==0:
            return 0
        return n
y= reduce(lambda x,y:x+checkprime(y),arr1) 
print(y)   