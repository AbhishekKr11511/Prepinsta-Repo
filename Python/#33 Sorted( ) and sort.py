even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11, 13, 15]

even.extend(odd)
print(even)
natural = sorted(even)
print(natural)


string1 = "Two driven Jocks help fax my big quiz"

result = sorted(string1)
# sorted() function sorts all the characters in ascending order based on their ascii value
print(result)
print(string1)

# list.sort() :- Sorts the list, doesn't make new object out of it.
# sorted(list) :- Creates a new list consisting of the elements in (list) sorted in ascending order. It won't change
#                   the list itself.


# We can also reverse parameter as well to sort in descending order

string2 = "Two driven Jocks help fax my big quiz"

# Sort in descending order
final = sorted(string2, key=str.casefold, reverse=True)
#                         ^                     ^
#                     <ignore case>     <reverse the list>
print(final)