users = {
    123: '@abhishek_123',
    124: '@satyam_234',
    125: '@varun_645',

}

print(users[123])
users[123] = '@brosev_823'
print(users)
print('\n')
# -------------------------------------
#1
for people in users:
    print(people)  # This will print the key of the dictionary
    print(users[people])  # This will print the value of the corresponding key in the dictionary
print('\n')
#2
for people in users:
    print("The id of people is : {} and their user name is : {}".format(people, users[people]))
print("\n")

#3
# If we only want to print the values
for i in users.values():    # We use value() function
    print("Usernames : " + i)
print('\n')

#4
# We can also use a function called items()
for x, y in users.items():  # This users.items() makes the dictionary into a tuple, x : key and y : value
    print(x, y)
print('\n')

keys_yes = users.keys()
print(keys_yes)
# This will print the keys from the dictionary

