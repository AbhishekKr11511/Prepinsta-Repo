# When an Object is Mutable, it means it can be changed.
# 1. List
# 2. Dict
# 3. Set
# 4. Bytearray

items = ["eggs", "bananas", "maggie", "apples", "bread", "curd"]

items_2 = items

print(items)
print(items_2)
print()
print(id(items))
print(id(items_2))
print()


items[2] = "juice"  # Here the 3rd element is replaces with "juice"

print(items)
print(items_2)

print(id(items))
print(id(items_2))
# As you can see that, even tho we completely changed an element in the list, there was change in the ID of items.
# Also the ID of items_2 also remains same, we didn't do anything to that reference.
# Same ID means, it's the same object, and clearly it holds a different value, So it is proved that lists are mutable.

