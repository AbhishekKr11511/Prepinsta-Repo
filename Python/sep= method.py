name = 'Abhishek'
age = 100

# If we run the print statement like below, it default adds a space between the parameters
print(name,age,'India',2020)

# However if we use the sep= method, just like end=, it will override the default and let you add your own separator
print(name, age,'India', 2020, sep="")  # If we don't add anything, it will not space

print(name, age,'India', 2020, sep="/")