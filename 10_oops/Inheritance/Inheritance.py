class A:
    def display(self):
        print("I am in class A")
    
    def get(self):
        print("Hello")

class B (A):
    def display(self):
        print("I am in Class B")

a = A()
b = B()

a.display()
b.display() 
b.get()