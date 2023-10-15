# The precision in any language means, till what decimal value will the numbers will be precise

print("{0}".format(22 / 7))
# The default precision after decimal is, 15

# Filled with function, states the number of space need to be filled in a string mandatory.
print("{0:100}".format(22 / 7))
# This just prints (50-15) blank strings, until 50 places are printed including the value of 22/7.
print(len("{0:100}".format(22 / 7)))  # See.. 50 is length of the whole string

# But get a load of this
print("{0:100f}".format(22 / 7))  # After 100 we write <f>, then we the value acts like a float in C.(6 decimal point)

print("{0:f}".format(22 / 7))  # Hence this format will give a default design of float
print("{0:.2f}".format(22 / 7))  # We refine it even more by putting <.2f>, this gives only 2 values after decimal

print("{0:.20f}".format(22 / 7))  # In this way we can even remove the default limit of the decimal places in python

print("{0:.100f}".format(22 / 7))  # Removing the limit we can see how long can python go in precision
print("{0:.51f}".format(22 / 7))  # If we count we get that 51 is the max precision in python for any numerical value

