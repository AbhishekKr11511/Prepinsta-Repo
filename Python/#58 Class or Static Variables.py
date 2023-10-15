
def increase_counter():
    Student.counter += 1

class Student:
    # All variables declared inside just the class not methods are class variables
    college = "IIT"     # Class Variable :- Declared inside a class
    counter = 0

    # All variables declared inside class METHODS are instance variables
    def __init__(self, name, roll_no):
        self.name = name         # Instance Variable :- They are assigned the value inside the method
        self.roll_no = roll_no   # Instance Variable :- """"
        increase_counter()


stud1 = Student('Abhishek', 12)
stud2 = Student('Satyam', 13)
stud3 = Student('Varun', 14)
stud4 = Student('Rahul', 15)



print(stud1.name)
print(stud1.roll_no)
print(stud1.college)
print()

Student.college = "NIT"     # This completely changes the variable for every object : - STATIC Change

print(stud2.name)
print(stud2.roll_no)
print(stud2.college)
print()

stud3.college = "BIT"       # While this will only change for that particular object itself  :- DYNAMIC Change

print(stud3.name)
print(stud3.roll_no)
print(stud3.college)
print()

print(stud4.name)
print(stud4.roll_no)
print(stud4.college)
print()

print("The number of students are : " + str(Student.counter))
