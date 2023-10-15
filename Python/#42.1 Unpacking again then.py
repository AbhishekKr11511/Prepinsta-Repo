for index, letters in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(index, letters)
# We know the above statement will print the index of each of the letters.


for letters in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(letters)
# This will print in the format of (0, a)  (1, b),
# We now know that after all this time enumerate function creates tuples of the elements
# Whenever we used enumerate function, we were actually unpacking the tuples

for letters in enumerate("abcdefghijklmnopqrstuvwxyz"):
    i, values = letters     # (0, a) ...
    print(i, values)
    # This gives the same result as we unpacked the index of the elements in 'i' and the letters in 'letter'

# Lets say we have a database of different plots of land over the country
# Each land plot, has a location, length , breadth and price per sq_meter

land = ('Delhi', 12, 100.0, 150.0)
#                ^     ^      ^
#            price, breadth,length
# We want the total price of the land

print(land[1]*land[2]*land[3])
# Rather than printing the above statement we can just unpack the elements

location, price_sqm , breadth, length = land
# We just unpacked the elements into different variables, in this way the program is looks good and also even if the
# attributes change we don't have to change any thing

print( price_sqm*length*breadth)    # same as line 25