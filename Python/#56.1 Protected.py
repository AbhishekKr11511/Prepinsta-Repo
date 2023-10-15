# Public variables are accessible all over the program
# Private members only accessible within the class or by methods of the class within
# Protected members are accessible within the class and its child classes
# And their methods and all.
# Single underscore is used to identify protected variables. '_'
# _variable :- protected variable

class Citizen:
    def __init__(self, aadhar):     # This is called a constructor, It doesn't return any value
        self.aadhar = aadhar        # It just maintain a database of the passed values in an organised way

    def get_aadhar(self):
        print(self.aadhar)


class Person:
    def __init__(self, name):
        self._name = name


    def print_value(self):
        print(self._name)

    def is_student(self):
        return False


# The child class can access all the functions and parameters of the parent class
class Student(Person, Citizen):
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


person1 = Person("Abhishek")
person2 = Student('Varun', 65, 1123)
person2.name = 'Satyam'
person1.print_value()
person2.print_value()
person2.get_roll()
person2.get_aadhar()
print("Parent is Student ? ", person1.is_student())
print("Student is a Student ? ", person2.is_student())