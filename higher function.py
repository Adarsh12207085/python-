def func1(param):
    return param.upper()
    y=func1
    print(y)
    print(y("computer"))
    def func1(param1):
     def func2(param2):
         return param1.upper()+param2.lower()
     return func2
y=func1("computer")
print(y)
print(y("science"))
def func1(func2):
     def func3(param):
         print(param.upper())
         func2()
         print("Department")
     return func3
@func1
def func2():
     print("science")
func2("computer")

