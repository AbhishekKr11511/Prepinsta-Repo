
#           0123456789012345678901
string_1 = "Hello Beautiful people"

# These operations are called "Slicing" of a String.
print(type(string_1)) # <str> is the data type

print(string_1[10])  # This will print the 10th element
print(string_1[:10])  # This will print till 10th element while excluding the 10th element
print(string_1[10:])  # This will print from 10th element to end while including the 10th element
print(string_1[5:10])  # This will print from 5th element to 10th, all above rule apply
print(string_1[-1])  # This will print the last element of the string
print(string_1[-3])  # This will print the 3rd last element.
print(string_1[0:-1])  # On this logic this should give the string excluding the last element
print(string_1[:])  # This will just print the whole string as is. If we don't assign the limits
print(string_1[0:22]) # Since there are 21 elements & string doesn't include last index -> Default prints all chars.
print(string_1[-22:]) # This also works
print(string_1[-4:2]) # We can't traverse through the string backwards normally like this.

# Step slicing of a string -> Basically the distance of skipping of elements
print(string_1[0:22:2]) # The 3rd parameter means, it will print every 2nd element (Hence skipping one element)
print(string_1[0:22:3])
print()
number = '1,423,612,624,245,864,345'     # What if we want to print only the commas while using step slicing
print(number[1::4]) # Since every comma is the 4 places away, we do not specify the later range so blank left.


# Quiz questions
"""
print("The sum of {0:b} and {1:x} is {2:o}".format(12, 1, 10))
print("Hello {0!r} {0!s}".format('Prep', 'insta'))
print('{:#}'.format(2221114443))
print("Hello {0[0]} and {0[1]}".format(('prep', 'insta')))
"""
