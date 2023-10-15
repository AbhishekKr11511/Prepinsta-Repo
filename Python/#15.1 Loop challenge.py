# We want to eliminate the special characters and print the only the numbers

number = '1,345:645;2,1564;,345,234,,345,34:789.231'
#         012345678901234567890     -> This shows the index
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


