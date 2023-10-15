# All the operators we can use in str type variables, we can use for lists as well.

string_1 = "Hello Beautiful people"  # This is a string variable

# Now we see how we can print the string in different ways
# 1.
print(string_1)
# 2.
for i in string_1:
    print(i, end="")  # Used end to print in the same line.
print()
# 3.
for i in range(len(string_1)):
    print(string_1[i], end="")
print()
# All the above statements print the same output
# -------------------------------------------------------------------------

string_2 = ["Hello Beautiful people"]  # This is a list.
# 1.
print(string_2)
# 2.
for i in string_2:
    print(i, end="")
print()
# 3.
for i in range(len(string_2)):
    print(string_2[i], end="")
print()

# As we can see both string variable and list variable work the same way
# -------------------------------------------------------------------------

#               0        1         2
string_3 = ['Orange', "Apple", "Banana"]
print(string_3)

print(string_3[1])  # This will print the second element of the list
print(string_3[1][3])  # This will print the 4th element-(character) of the 2nd element of the list
# -------------------------------------------------------------------------

day = "sunday"
print("day" in day)     # True, because <in> means if day is a sub string of the string sunday
print("fri" in day)     # False, because <in> means if fri is a sub string of the string sunday
print("Sun" in day)     # False, because python is case sensitive.

