#          0  1   2    3    4    5    6    7    8    9    10    11     12
'''
numbers1 = [3, 7, 200, 201, 203, 214, 281, 300, 301, 302, 309, 40001, 40009]
print(numbers1)

# del is an in-built function to delete elements from list and string
del numbers1[0:2]
print(numbers1)

del numbers1[8]
print(numbers1)

m = max(numbers1)
print(m)

'''
# Let's say we only want to store values greater tha 200 and less than 4000
list1 = [3, 7, 200, 201, 203, 214, 281, 300, 301, 302, 309, 40001, 40009]

for index, value in enumerate(list1):
    if (value < 200 ) and (value > 4000):
        del list1[index]
        print(f"{index}. {value} is deleted")
    else:
        continue
