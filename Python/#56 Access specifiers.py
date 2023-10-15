class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_val(self):
        print(self.name)
        print(self.id)


s1 = Student('Abhishek', 1)
s1.print_val()

# We can easily change the value of instances like this
s1.name = 'Hacker'
s1.id = 666
s1.print_val()
print('\n')

#-------------------------------------------------------------------------------------
# This is not favourable as, data can be easily edited leading to loss of data
# This can be solved however, if we protect or private the data. This prevents this from happening

# We create private the variable by adding double underscore before the name of the variable. '__'

# __variable :- private variable
class Student:
    def __init__(self, name, id):
        self.__name = name  # Adding __ before the variable to make them private
        self.__id = id

    def print_val(self):
        print(self.__name)
        print(self.__id)


s1 = Student('Abhishek', 1)
s1.print_val()
s1.name = 'Hacker'
s1.id = 666
s1.print_val()  # You can see that the values didn't change. that's the power of privation the variables

#-------------------------------------------------------------------------------------------

