# Sets are written in curly brackets like dictionaries, but they are different than dictionaries
# They are unordered and do not have indexes, to their elements
# They are iterable though
countries = {'India', 'USA', 'UK', 'Spain', 'Germany'}

# print(countries[0]) -> this will give error

for country in countries:  # Run this statement again & again watch the order that they are printed change randomly.
    print(country)

# This way they don't consume extra memory or time, as there is no need to reorder or reshuffle them.

# So why would we use Sets over other sequence types?

print('USA' in countries)
print('\n')
# Here is an example where we don't care about the order, but if the element is present in that set or not
# -------------------------------------------------------------------

# Add item in sets

countries.add('China')
print(countries)
print('\n')
# "China" has been added, when we print the modified set, we can see China is randomly placed in there
# Again because there is no order, we don't need to use the .append() function, as it adds the element to the end.

# -------------------------------------------------------------------
# Update method in sets

countries.update(['Italy', 'France', 'Cuba'])  # Make sure to use [] before typing the items
# Or it will add the individual string (letters) separately
print(countries)
print(len(countries))
print('\n')

countries.pop() # This generally removes the last element or the i'th index element ( That won't work as sets don't
# have indexes)
# Therefore pop() will remove a random item from the set
print(countries)

# However since .remove() function takes the actual item as the argument, it will remove that item, wherever
# It might be present

countries.remove('China')
print(countries)


