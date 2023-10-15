# Dictionary is form of list in form of a key : value pair.
# They are also mutable.


dict = {
    "mangoes": "Fruits which are sweet and yellow",
    "apples": "Round red fruits, also very sweet",
    "water melon": "Big round watery fruits, green on the outside and red on the inside",
}

dict2 = {
    "pencil": 10,
    "erasers": 5,
    "sharpener": 2,
    "paper": 100,
}

print(dict)
print(dict['apples'])   # We have specified the key, so it will print the corresponding value

print(dict2)
print(dict2["pencil"])  # same