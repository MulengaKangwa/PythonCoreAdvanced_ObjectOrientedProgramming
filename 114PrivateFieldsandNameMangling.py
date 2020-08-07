# This is the start of the videos on encapsulation.
class Student:
    def __init__(self):
        self.__id=123 # These field cannot be accessed directly, as they have been private
        self.__name="John"
    def display (self):
        print(self.__id) # Using the display method allows you to overcome the fact the field is private
        print(self.__name)
s = Student()
s.display()
print(s._Student__name) # This is name mangling. In other words, it allows the script to access syntax that is private