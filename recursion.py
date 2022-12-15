def factorial(n):
    if n==1:
        return 1
    else:
        return n *factorial(n-1)
n=int(input("enter the number"))
print("factorial", factorial(n))
#stack-- person who is first will go last.when we call a function like 5 first then it will be go at las
n= int(input("enter the value"))
ans=1
while n>1:
    ans*=n
    n=n-1
print("factorial",ans)