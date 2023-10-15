class Student:
    roll_no = 0
    name = 'Unknown'


class Users:
    id = 1233546
    username = 'string'
    lists_pages = 15


# What if a Student named 'Abhishek' needs to be created

student1 = Student()   # A simple method
student2 = Student()

student1.name = 'Abhishek'  # Here we pass the values to instances
student1.roll_no = 2

print(student1.name)
print(student1.roll_no)

print(student2.name)    # Since the values are not assigned to the instances hence prints the default values
print(student2.roll_no)

user1 = Users()
user2 = Users()

# Same could be done with other classes as well

# As you can see that when we need to create more than like 1000s of objects, We can't individually create each
# object. There is a method to create multiple objects easily

