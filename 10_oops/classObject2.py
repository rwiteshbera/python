class Student:
    name = ""
    roll = 0

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setRoll(self, roll: int) -> None:
        self.roll = roll

    def getRoll(self) -> int:
        return self.roll
    

student1 = Student()

student1.setName("Rwitesh")
student1.setRoll(21)

print(student1.getName() + " " + str(student1.getRoll()))


