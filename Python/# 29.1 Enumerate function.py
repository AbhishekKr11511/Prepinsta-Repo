# Often, when dealing with iterators, we also get need to keep a count of iterations.
# Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or converted -
# into a list of tuples using the list() function.

stock = ['exit',
         'butter',
         'bread',
         'milk',
         'coffee',
         'biscuits',
         'yogurt',
         'cream']

number = enumerate(stock)
'''
print(list(enumerate(stock)))
# Here we see that every element has their index attached to them. This is the default result of enumerate

print(list(enumerate(stock,1)))     # We can modify the parameters a little by specifying the 1st index
'''
print("Add items from the following available items")
for item in enumerate(stock):
    print(item)

for num, item in enumerate(stock):
    print(f"{num}. {item}")

# We can format it and take the index in another variable, hence we can use interations in this way.
