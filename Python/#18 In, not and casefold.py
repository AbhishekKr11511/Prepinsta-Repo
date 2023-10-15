name = "Hello Beautiful People"

letter = input("Enter the string : ")
letter = letter.lower()
# What this will do is lower case all the entered string for better comparison as python is case sensitive.

if letter in name.lower():  # This will also help in the comparison
    print("The entered string is in the name")
else:
    print("Its not there ")

