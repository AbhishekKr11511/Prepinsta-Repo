even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# If we want to make a nested list containing both the even and odd lists, but separately
numbers2 = [even, odd]
print(numbers2)
# Now numbers2 is a nested list containing 2 separate lists

# Now if we want to print a nested using for loop

for i in numbers2:
    for j in i:
        print(j, end=" ")
    print()

'''
# If we merge both lists into 1 list this is how we do it
numbers1 = even + odd
print(numbers1)
'''
