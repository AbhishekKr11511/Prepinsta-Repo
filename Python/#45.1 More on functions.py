
'''
def myfunction(first_name="Unknown"):
    print(first_name + " Grover")


myfunction("Abhishek")
myfunction("Varun")
myfunction("Satyam")
myfunction()  # When no argument is passed then the function will take the default value which is 'Unknown'
'''
'''
def my_function(fruits):
    for fruit in fruits:
        print("I love " +fruit)


fruits = ['water melon', 'oranges', 'apples']

my_function(fruits)
'''

def my_print_func(first_name, last_name, age, sep_val, end_val):
    print(first_name, last_name, age, sep=sep_val, end=end_val)


my_print_func("Abhishek", "Johns", 23, "__", ' @\n')  # We are trying to define pass our own sep and end values
my_print_func("Varun", "Grover", 24, "__", ' @\n\n')  # We are trying to define pass our own sep and end values
#------------------------------------------------------
def my_function(val):
    val = [12,23,34]    # New object is created so even tho we pass the value of list1 it wont change
 #   val[0] = 0
    print(val[0])
    return val  # However if we return the new formed object, this will printed
    pass


list1 = [10, 20, 30, 40, 50]
my_function(list1)
print(list1)    # But the change doesn't occur here.
print(my_function(list1))   # We print the return value here
print()

#-----------------------------------------------------

def swap(a, b):
    a, b = b, a     # We can just swap like that in python, no need of a temp variable.
    return a, b


x = 10
y = 20
print((x, y))
#print(swap(x, y))  # This also works
x, y = swap(x, y)   # We are returning 2 values so we reference the 2 variables
print(x, y)

#------------------------------------------------------