# We can assign values to variables in a single line as well in python

x, y, z = "Hello", "my name is", "John." # Here the values are assigned respectively.
print(x+" "+y+" "+z)


#    Python has 3 type of numeric data types
#   -> int , also there is no limit of how big an int can be unlike C. As long as the total memory can handle it.
#   -> float
#   -> complex

# We can also write binary, hex and octal values in python, we only have to use a specific prefix

# binary prefix is 0b or 0B
# octal prefix is 0o or 0O
# hex prefix is 0x or 0X

# But if we look at the data type it will only show <int>
print(0b1000)
print(type(0b1000))
print(0o1000)
print(type(0o1000))
print(0x1000)
print(type(0x1000))

# Some operations with float values

a = 1.79e5 # e5 means mutiplying the number by 10^5.
print(a) #179000.0 will be printed as a is a floating value.

