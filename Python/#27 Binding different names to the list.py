items = ["eggs", "bananas", "maggie", "apples", "bread", "curd"]

items2 = items

list1 = list2 = list3 = list4 = items
# Every one of these variables will act as a reference to values of the list 'items'

items.append("butter")
# We add an element called "butter"

print("items has :", items)
print("list 4 has :", list4)
# We can see all the list* variables has the same values
