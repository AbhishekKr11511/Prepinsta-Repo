# __init__ :-

class Student:
    def __init__(self, name:str = 'Unknown', roll_no:int = 0, tot_marks :int = 0):
        self.name = name
        self.roll_no = roll_no
        self.tot_marks = tot_marks
    def cal(self):
        return self.tot_marks/5


class Users:
    def __init__(self, id:int, username:str, pages:int):
        self.id = id
        self.username = username
        self.pages = pages




student1 = Student('Abhishek', 12, 438 )
student2 = Student('Satyam', 76, 418)
student3 = Student()      # No arguments is passed will yield the default value, if now default value, yields error.

print(student1.name)
print(student1.roll_no)
print(Student.cal(student1))
print('\n')

print(student2.name)
print(student2.roll_no)
print(Student.cal(student2))
print('\n')


print(student3.name)        # Prints the default value
print(student3.roll_no)


# Input all the values of the instances.
id1 = int(input("Enter id : "))
username1 = input('Enter username : ')
pages1 = int(input('Enter number of pages : '))

user1 = Users(id1, username1, pages1)
print(user1.id)
print(user1.username)
print(user1.pages)
