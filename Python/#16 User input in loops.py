# We can take user input and then run the loop as well, Here's how :-

number = input("Enter something : ")

value = ""
symbals = ""
for i in number:
    if i.isnumeric():
    # This function checks if the string is numeric or not
        value += i
    else:
        symbals += i

print(value)    # Prints the numeric values
print(symbals)  # Prints the special characters


