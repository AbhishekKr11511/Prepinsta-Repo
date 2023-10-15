# Let's say we only want to store values greater tha 200 and less than 4000

#        0  1   2    3    4    5    6    7    8    9    10    11     12
list1 = [3, 7, 200, 201, 203, 214, 281, 300, 301, 302, 309, 40001, 40009]

min = 200
max = 4000
'''
for index, value in enumerate(list1):
    if (value < min) or (value > max):
        del list1[index]
        print(f"{index} -> {value} is deleted")
    else:
        continue

print(list1)
'''
start = 0

# Start removing the elements from behind or backwards, so that we don't face the problem of decreasing index
# Which will leading to skipping elements, which we don't want. We need to read every element

for i in range(len(list1)-1, -1, -1):
    if list1[i] < min or list1[i] > max:

        # If trying to print the actual deleted value, do it before deleting it.
        # Because after deletion the value will no longer be there in the list to be printed
        print("{0} is removed".format(list1[i]))
        list1.pop(i)
    else:
        continue

print(list1)


