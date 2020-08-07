class Student:
    def setId(self,id): # @ReservedAssignment
        self.id = id

    def getID(self):
        return self.id

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

s = Student()
s.setId(123)
s.setName("John")
print(s.getID())
print(s.getName())


