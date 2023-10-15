# Encapsulation -  It describes the idea of wrapping data and the methods that work on some data within one unit.
# This puts restrictions on accessing variables and methods directly & can prevent the accidental modification of data.

# Abstraction - Abstraction is used to hide the internal functionality of the function from the users.
# The users only interact with the basic implementation of the function, but inner working is hidden.
# User is familiar with that "what function does" but they don't know "how it does."

# Abstraction and Encapsulation work hand in hand.

# Now what if we take the data for a huge amount of users, let's say like 100,000,000. We can't manually make
# That many variables . Thousands of people sign-up on websites, how does that work?
# -----------------------------------------------------------------------------------------------------------------------

# Objects as Lists
# We make an object list to get the data about the student, since we don't want to manually keep creating objects
counter = 0


class Student:
    def __init__(self):     # This is the default data, we will not use this
        self.name = "Unknown"
        self.roll_no = 0

    def set_data(self, name, roll_no):      # WE use this to actually set data for each object in the list
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self):         # This returns just the name. All are private variables
        return self.__name

    def get_roll(self):         # This returns the counter or roll_no. All are private variables
        return self.__roll_no

    def get_values(self):
        return self.__name, self.__roll_no


stud_obj_list = [Student() for i in range(4)]       # This declares an object list of give range
def fetchValues():      # This function is used to input values from the user
    global counter
    counter += 1
    temp_name = input("Enter name : ")
    return temp_name, counter   # Returns the counter and Name

for i in range(0, len(stud_obj_list)):      # Loop for inputting the values
    x, y = fetchValues()        # We pass the function to get values
    stud_obj_list[i].set_data(x, y)     # Set_data is called to store these values in an object


for i in range(0, len(stud_obj_list)):      # Loop for printing all the inputted names with their roll_no
 #   print(stud_obj_list[i].get_name())
 #   print(stud_obj_list[i].get_roll())
    print(stud_obj_list[i].get_values())


