even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11 , 13, 15]

# list1.extend(list2) adds the elements of list2 to list1.

even.extend(odd)
print(even)
new_list = even
print()
# list.sort() function sorts the elements in ascending order
even.sort()
print(even)
print(new_list)
# We also see that list are mutable as well.

