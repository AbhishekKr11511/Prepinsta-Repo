# Let's use the gained knowledge from the previous module

for i in range(1,11):
    print("No. {0} squared is {1} and cubed is {2} ".format(i, i **2, i**3))

print()

for i in range(1,11):
    print("No. {0:2} squared is {1:3} and cubed is {2:4} ".format(i, i **2, i**3))
#                 ^                ^                  ^
# These are the black string (which is just a space) we are trying to print to make the output
# Look pleasing and orderly. The max digit is 2 in number place, 3 in square place and 4 in cubed place,
# That's why the numbers
print()

for i in range(1,11):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4} ".format(i, i **2, i**3))

# Using < operator we left align the values
# Using ^ operator we middle align the values

