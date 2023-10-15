# Inheritance :- It helps build relationship b/w classes/objects in real world scenarios, promotes code re-usability
# getters and setter :-
# Access specifiers

# We create a super class/parent class, Person.

class Citizen:
    def __init__(self, aadhar):     # This is called a constructor, It doesn't return any value
        self.aadhar = aadhar        # It just maintain a database of the passed values in an organised way

    def get_aadhar(self):
        print(self.aadhar)


class Person:
    def __init__(self, name):
        self.name = name


    def print_value(self):
        print(self.name)

    def is_student(self):
        return False


# The child class can access all the functions and parameters of the parent class
class Student(Person,
              Citizen):  # We write the parent class in brackets to tell python it is subclass of the class in brackets
    def __init__(self, name, roll_no, aadhar):
        self.roll_no = roll_no

        Person.__init__(self, name)
        Citizen.__init__(self, aadhar)

    def get_roll(self):
        print(self.roll_no)

    def get_aadhar(self):
        print(self.aadhar)

    def is_student(self):
        return True


person1 = Person("Abhishek")  # We make an object in Parent class
# WE can see below, Multiple inheritance
person2 = Student('Varun', 65, 1123)  # We make an object in child class, It also inherits both Person and Citizen
person1.print_value()
person2.print_value()  # Still works because it can access the parent class methods
person2.get_roll()      # We have to create to function in Student class to print this
person2.get_aadhar()
print("Parent is Student ? ", person1.is_student())
print("Student is a Student ? ", person2.is_student())
