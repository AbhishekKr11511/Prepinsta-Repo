class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


user1 = User("Priyam", 9813732323)
print(user1.name, "-", user1.phone)

user1.name = "You have been hacked"
user1.phone = 99999999999
print(user1.name, "-", user1.phone)
print('\n')


# As we know, by sql injection or other operation, hackers can inject their own code, to mess with the program
# Therefore we private these variables to prevent this
# _____________________________________________________________

# But we can use getter and setter method to access even these private variables

class User:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return "Mr." + self.__name

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone


authentication = 123
user1 = User("Priyam", 9813732323)
# We use the get method to even access the private variable, that's how getters work
print(user1.get_name())
print(user1.get_phone())
print()
user1.name = "You have been hacked"
user1.phone = 99999999999
print(user1.get_name())  # Can't change OMEGA LUL
print(user1.get_phone())
# The above changing the data doesn't work as they are private
# As you can see the data is safe.

print('\n')

# Here we can actually change the name, by using the setter method. so Setters can even change the private data
user1.set_name("Abhishek")
user1.set_phone(8987393345)
print(user1.get_name())
print(user1.get_phone())
