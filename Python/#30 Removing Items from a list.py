# We will the functioning of .pop(i) and .remove(x)

# .pop(i) this function removes the i'th index element from the list
# .remove(x) this function removes the 1st element which matches with the x, from the list.
# Taking the same example from before.
stock = ['butter',
         'bread',
         'milk',
         'coffee',
         'biscuits',
         'yogurt',
         'cream',
         'yogurt']
'''
print(list(enumerate(stock)))
print()

print("Removing the index 3 element")
stock.pop(3)
print(stock)
print()

print("Removing a specific value from the list")
stock.remove('cream')
print(stock)
'''
print(list(enumerate(stock)))
print()

index = int(input("Enter the nth element to remove = "))
stock.pop(index)
print(stock)
print('\n')

try:
    element = input("Enter an element to remove = ")
    stock.remove(element)
    print(stock)
except ValueError:
    print("This element does not exit in the list")