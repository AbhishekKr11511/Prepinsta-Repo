# Tuples are just like lists, but the difference is that they are Immutable (Unchangeable)
# Also tuples are denoted by round brackets (), whereas lists are denoted by square brackets []
# That also means that the hidden methods or magic methods don't work on tuples which changes them in any way.
# Because of this tuples consume less memory than lists, so huge amounts of data is much preferably stored in tuples
# This also means that the execution of the program is also faster
# Integrity of data is protected, So errors are much preferred rather than losing the data itself.

tup = 'a', 'b', 'c', 'd'
print(tup)

name = "Abhishek"
age = 23

#print(name, age, "USA", 2023)

info = name, age, "USA", 2023
print(info) #This will print a tuple
print(info[0])
print(info[1])
print(info[2])
print(info[3])

# What if we try to change the value
#info[2] = 34
#TypeError: 'tuple' object does not support item assignment


