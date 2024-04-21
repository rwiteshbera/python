class Student:
    # It runs as soon as an object of a class is instantiated.
    def __init__(self, name, roll : int) -> None:
        self.name = name
        self.roll = roll

    def getName(self) -> str:
        return self.name

    def getRoll(self) -> int:
        return self.roll
    

rwitesh = Student('rwitesh', 21)
print(rwitesh.getName())
print(rwitesh.getRoll())



