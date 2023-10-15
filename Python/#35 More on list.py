stock = ['butter',
         'bread',
         'milk',
         'coffee',
         'biscuits',
         'yogurt',
         'cream']
print(stock)

# Replaces the 4th index element
stock[4] = "cheese"
print(stock)

# This will replace and append onwards the 5th index element
stock[5:] = ['sugar', 'ghee', 'flour', 'oil']
print(stock)

# This will replace and append before the 4th index element
hardware = ['battery', 'screw', 'hammer']
stock[:4] = hardware
print(stock)
print('\n')
#-------------------------------------------------------------

stock_2 = ['butter',
         'bread',
         'milk',
         'coffee',
         'biscuits',
         'yogurt',
         'cream']
# insert()

stock_2.insert(1, 'eggs')   # Adds 'eggs' at that index and pushes all the elements after that.
print(stock_2)