grocery = ["eggs",
           "bananas",
           "maggie",
           "apples",
           "bread",
           "curd",
           "peas"]

for item in grocery:
    print(item)

print(grocery[3])
print(grocery[1:4]) # 4th element not included as usual.

print(grocery[::2]) # Prints alternate items

# All the rules which apply to string or range() applies here as well.
