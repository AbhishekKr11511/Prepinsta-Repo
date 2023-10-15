# Below we have dictionaries in a single dictionary.

students = {
    'child1': {
        'name': 'Abhishek',
        'age': '23',
    },
    'child2': {
        'name': 'Satyam',
        'age': '24',
    },
    'child3': {
        'name': 'Varun',
        'age': '22',
    },
    'child4': {
        'name': 'Rahul',
        'age': '25',
    },
}

print(students)
print('\n')

for children in students:
    print(children,':', students[children])

print('\n')

for children in students.values():  # We first go inside the value part of the dictionary as it has the nested
#                                            dictionary.
   # print(children)
    for details in children.items():    # Gives a tuple
        print(details)
    print()