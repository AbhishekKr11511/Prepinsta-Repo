# String Replacement field

weight = 70
print("My is weight is : ", weight)     # This works like c
print("My is weight is : "+str(weight))    # This works as we convert the <int> to <str> cohesive with the rest of
# the statement

# These below are called string replacement fields.

print(f"My is weight is : {weight}")    # Here we use the formatting style to print different data types
print("My is weight is : {0}".format(weight))  # Here we also use the <format> function, with weight as the argument


# All the above statements print the same thing
# -------------------------------------------------------------------------

# We can also pass multiple args in the string replacement field function

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7} ".format(31, 'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'))
# As we can see in the above statement that we can even pass different data types and python will recognise them easily

print("There are {2} days in {0}, and {1} days in {3}".format('May', 30, 31, 'June'))
print(" Jan : {0}, Feb : {1}, Mar : {0}"
      " Apr : {2}, May : {0}, Jun : {2}"
      " Jul : {0}, Aug : {0}, Sep : {2}"
      " Oct : {0}, Nov : {0}, Dec : {0} ".format(31, 28, 30))
# We have to make sure that the order is actually considered
# {0} will take the 1st argument and {1} will take the 2nd and so on....
# Doesn't matter how they are place in the print() statement.
# We can also reuse the arguments in the format() function as we can see in the last line of code.
