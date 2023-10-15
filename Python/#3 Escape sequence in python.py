# \n  \t  \b  \r  -> We will learn these

string_1 = "I am\na string\nin multiple lines\n"
print(string_1)
# \n is the annotation for the new line.

string_2 = "1. Oil\t2. Flour\t3. Bake\t4. Oven"
# \t is the annotation for the tab space

# The best way to print a string with multiple "'"'s is to include them triple """ or '''

print("""Hello my 'name' is going to "kill" me so stay away from my niece's cat. whatever that mean's.""")
# the above statement doesn't make any sense but it does show there is no problem to min max the Quotes in there.

string_3 = """I am
again a string
spanning in 3 lines"""

print(string_3)

# Let's say we want to print the path of a file.
# C:\User\temp\new_course.pdf  -> This is the said path of the file.
# We won't be able to use the <\> here, as it is used as bulletin in print statement (separator or new line etc)
# so we can use <\\> to solve this problem.
print("C:\\User\\temp\\new_course.pdf")

# Or we can use <r> in before the string outside the quotes to print as is
# writing <r> in front of string means Raw String.

print(r"C:\User\temp\new_course.pdf")
print("\n")
# This also solves the problem.

# <\b> this is used for Backspace.

print("Hello\b world") # This will omit the character just before <\b>
# Hell World

print("Hello\b\b\b\b\b\bworld") # Multiple of these
# world

# \r Carriage Return
print("Hello \rworld")
