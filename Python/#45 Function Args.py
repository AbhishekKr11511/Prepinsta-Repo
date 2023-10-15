'''
def name(*args):
    print("your name is {0}".format(args[1]))


name('abhishek', 'pritika', 'satyam')'''


# -------------------------------------------

def name(*args):
    for arg in args:
        print("your name is {0}".format(arg))


name('abhishek', 'pritika', 'satyam')
# These are keywords arguments

# *args is used in python when we don't know how many parameters are going to be passed in the function
# Yes the nature of the operation will remain the same

