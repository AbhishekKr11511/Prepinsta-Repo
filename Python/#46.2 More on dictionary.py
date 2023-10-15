users = {
    123: '@abhishek_123',
    124: '@satyam_234',
    125: '@varun_645',
}

print(len(users))


# We can also add key:value pairs in dictionaries like done below
users[126] = '@kaushik_34'
users[127] = "@angali_123"

#print(users)

for x, y in users.items():
    print(x, y)
print('\n')
#--------------------------------------------------------------------------
# How we can remove a pair in dictionary?

del users[126]
for x, y in users.items():
    print(x, y)
# We can see that we can remove the pair by using the key
print('\n')
#--------------------------------------------------------------------------
x = users.pop(123)  # It pops the value in  the variable x.
print(x)
print('\n')

#--------------------------------------------------------------------------
y = users.popitem()     # This command pops the last key:value pair
print("popped value : ", y )    # This also yields a tuple type variable
print()
for x, y in users.items():
    print(x, y)
print('\n')
#--------------------------------------------------------------------------
# We can copy a dictionary into another dictionary by using the dict() method, can also be done by .copy() method

user1 = dict(users)
user2 = users.copy()
print(user1)    # Both function the same way
print(user2)
print('\n')
#---------------------------------------------------------------------------
# Using a constructor to assign the values in a dictionary

students = dict(brand = "Harley", model = 'Street 750', fuel_type = 'petrol')
# We don't need quotes for keys
# We assign the value to the keys with the dict() function as well. Thus we created a dictionary
for x, y in students.items():
    print(x ,":", y)


