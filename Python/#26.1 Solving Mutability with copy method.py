items = ["eggs", "bananas", "maggie", "apples", "bread", "curd"]

items_2 = items.copy()

print(items)
print(items_2)
# The actual contents of the both lists are same
print()

print(id(items))
print(id(items_2))
# But if take a look at the IDs, its different
print()

items.append("butter")
items_2.append("Suger")

print(items)
print(items_2)

print()

print(id(items))
print(id(items_2))
print("\n")
# We see that yes even after appending new elements in the list the IDs didn't change.

# .copy() method copies all the contents of a list into another new list, hence making a new object with its own ID

