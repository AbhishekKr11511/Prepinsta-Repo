fruits = [
    'apple',
    'banana',
    'oranges',
    'mangoes',
    'litchi',
    'melon',
]

for fruit in fruits:
    print(fruit)

# We define a string type variable which will separate all the elements in list
separator = ' + '

# We use the join method with the said separator into a new list <value>, what this will do is run a loop
# .join() takes a iterable variable as its argument, with this we don't need to create any for loop to append the
# elements in a new list.

value = separator.join(fruits)
print(value)

# also .join() can only run on string type variables

