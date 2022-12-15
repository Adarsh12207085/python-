#multiple
"""class A:
    def Ainfo(self):
        print("A")

class B:
    def Binfo(self):
        print("B")
class C(A,B):
    def Cinfo(self):
        A().Ainfo()
        print("C")
        B().Binfo()
Cobj=C()
Cobj.Cinfo()"""
#multilevel
class A:
    def Ainfo(self):
        print("A")

class B(A):
    def Binfo(self):
        print("B")
        A().Ainfo()

class C(B):
    def Cinfo(self):
        print("C")
        B().Binfo()
        
Cobj=C()
Cobj.Cinfo()
"""class A:
    def Ainfo(self):
        print ("A")
class B(A):
    def Binfo(self):
        print("B")
        A().Ainfo()
Bobj=B()
Bobj.Binfo()"""
        



    