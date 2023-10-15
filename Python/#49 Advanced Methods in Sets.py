set1 = {'a', 'b', 'c', 'd', '$'}
set2 = {1, 2, 3, 4, '$'}

# Union -> Combines 2 sets .

set3 = set2.union(set1)  # We are merging the items and storing in another set(3)
print(set3)

# We can also merge the elements and store in just one of the native sets
set1.update(set2)  # just use the update method
print(set1)
print(set2)

# We also see that same items do not copy, if there is already that element present in the set.
# Because this is not addition, but a Union

# Intersection -> What is actually common items in all the sets.
# Difference -> Only keeps the unique items in the native set.

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = { 7, 8, 9}
set4 = set_1.intersection(set_2)
print(set4)  # Gives {4,5,6} as they are the only common element in both the sets

set5 = set_1.difference(set_2)
print(set5)     # Subtracts all the common elements from the self set.
#---------------------------------------------------------------------------------
# isdisjoint() This returns True or False if the sets are joint or not
val = set_1.isdisjoint(set_2)
print(val)
# Yields True if the sets are separate and false if the sets are joint

#---------------------------------------------------------------------------------

circle = {11, 22, 33, 44, 55}
circle2 = {22,33,55}
circle3 = {11,22,55,77,88}
# issubset This returns True or False if all the elements of the argument set are present in the native set

val2 = circle2.issubset(circle) # Is circle2 is a subset of circle?
print(val2)   # True

# .symmetric_difference() returns the unique elements of the sets, excluding the common elements
val3 = circle3.symmetric_difference(circle)
print(val3)