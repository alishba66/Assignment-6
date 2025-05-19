class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):  
    pass

d = D()  
d.show()  


print("MRO:", [cls.__name__ for cls in D.__mro__])
                          
        