a = b = c = d = e = 10
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print()
# The above statements will give the same id because all of them are just references to the same object.
a = 20
# Here we changed the value, since integer values are not mutable either, it will create a new object having a
# Different id or address
print(id(a))


# UNPACKING

x, y, z = 1, 2, 3,  # The values are assigned respectively to the corresponding variable
# Let's talk about the tuple unpacking
print(x)
print(y)
print(z)
print('\n')

values = 4, 8, 5,   # This is tuple
u, v, w = values    # Assigning their values
# The variables must be as many as the elements present in the tuple, no more no less, or it will give error
# 3 values are there, therefore 3 variables are a must. This also applies on any Sequence type as well.
# All the values of any sequence type variable, must be unpacked, if we are even unpacking a single one.

print(values)
print(u)
print(v)
print(w)

# Hence there is chance of mutability in variables like list, unpacking can be confusing as more elements could have
# been added after we did the unpacking. But this is not in the case in tuples due to its immutability
# Use tuples more for unchangeable data

