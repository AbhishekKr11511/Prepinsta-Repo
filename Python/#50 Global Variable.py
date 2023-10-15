name = "Abhishek"  # Global variable, accessible to every function and main


def myFunction():
    #print("1", name)
    name = 'Satyam'  # Local variable, Scope is limited to the function only.
    # This is a new variable itself. In new memory with a new id.
    print('2', name)


print('3', name)
myFunction()
print('4', name)    # Even after function call, still name = 'Abhishek'

print('\n ')
# ---------------------------------------------------------------------------------------
name = "Abhishek"   # Changes to 'Satyam' after line 19

def myFunction():
    global name  # When we use the global key word, It reassigns the value of the global variable itself
    print("1", name)
    name = 'Satyam'
    print('2', name)

print('3', name)
myFunction()
print('4', name)    # name = 'Satyam' , Here