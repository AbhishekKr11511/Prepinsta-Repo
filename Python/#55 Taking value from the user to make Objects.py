counter = 0


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def print_value(self):
        print(self.name)
        print(self.roll_no)


def fetchValues():
    global counter
    counter += 1
    temp_name = input("Enter name : ")
    return temp_name, counter


x, y = fetchValues()    # Call this function to enter variables and return them into the x and y
s1 = Student(x, y)      # Make an object from the arguments taken from the user

a, b = fetchValues()
s2 = Student(a, b)

s1.print_value()  # Since the object are of the Student Class, we can just call the functions of that class like that
s2.print_value()

