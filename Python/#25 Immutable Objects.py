# When an Object is Immutable, it means it can not be changed.
# 1. int
# 2. float
# 3. Bool (subset of int)
# 4. Str (string)
# 5. Tuple
# 6. Frozen set & Bytes

# The Basic Idea is, The value of pi is = 3.1415 , if we add or subtract or do anything to it, it won't be pi anymore
# 1 thousand is = 1000, if we add 1 to it, it becomes = 1001, Its no longer 1k anymore
# That's what Immutable means

"""
Everytime we create an object, a unique ID is attached to that object. It is not the same as address in C, but
kinda acts in a similar way
Python says, that ID, shouldn't necessarily be objects address. It only says that, ID must not change,
throughout the lifetime of that object, and it must be guaranteed

1. Cpython however, returns the address but not all versions of python will do that
2. However, if Python has to destroy the object and create it again (obviously same value), then it will change.
3. The ID of an object, can change everytime you run the program again, however, while the program
    is running it won't change.
"""
# Let's see how this works in python

result = True
result_2 = result

print(id(result))
print(id(result_2))
print(result)
print(result_2)

# The above statements gives the same ID number. Why?
# It's because the value : True is stored in the variable 'result'. The name of variable 'result' just acts as a
# reference name for the value : True.
# When we assign result to result_2, what happens is we applying another reference name for the value : True
# There is no creation of a new object. Therefore it prints the same ID

print()

# When we change the value itself the ID changes here, because changing the value creates a new object itself
result = False
print(id(result))

# While we see that the former reference result_2 is still pointing the value : True
print(id(result_2))

print(result)
print(result_2)

# If you try to change the value of an immutable object, rather than changing the actual, it creates a new object.
# Which will have it's own ID
# Hence we prove that Bools are immutable type.