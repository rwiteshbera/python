# Multilevel inheritance is a feature in object-oriented programming where a class inherits from another class, and then another class inherits from that class, creating a chain of inheritance. In Python, this means that a subclass can inherit from another subclass, forming a hierarchical relationship between classes.

class A:
    def a(self):
        print("I am in A")

class B(A):
    def b(self):
        print("I am in B")

class C(B):
    def c(self):
        print("I am in C")

c = C()

c.a()
c.b()