python = 1
# Python = True     -> Same meaning, Also any non-zero value works as True, See for your self, try -12.45

if python:
    print("Good, you know python")
else:
    print("Learn python")

name = ""
# name = False    -> As the string is empty, it returns false.
if name:
    print(f"Your name is : {name}")
else:
    print("What is you name? Try again...")
