class A:
    def display(self):
        print("I am in A")

    def m(self):
        print("Wow")

class B:
    def getData(self):
        print("I am in B")
    
    def m(self):
        print("Yeah")

class C(A,B):
    pass


C().display()
C().getData()

C().m() # Wow 
#When you have a class hierarchy like C(A, B), Python follows a method resolution order (MRO) to determine which implementation of a method to use when there are multiple inheritance conflicts. In your case, C(A, B) means C inherits from A first, then B. So, when you call C().m(), Python will look for the m method in A first according to the MRO. Since A has the m method, it prints "Wow".