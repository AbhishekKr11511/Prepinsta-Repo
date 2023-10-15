sentence = "You are going to be the best coder you have ever been after this course."

# .split() function splits all the individual strings (words) in a long sentence where words are separated by a space.
# And then it can also pass those individual words in a separate list, to create a new list of words of that sentence.
words = sentence.split()
print(words)

# Space is default character split() looks for to split the string
# This works on individual strings, but it will not split the individual letters as they are separated by space
some_words1 = 'Abhishek'
letters1 = some_words1.split()
print(letters1)

# If we separate them then it works fine.
some_words2 = 'A b h i s h e k'
letters2 = some_words2.split()
print(letters2)

# If we specify the split attribute
# Here we specified that whenever split gets a ',' it will spit right there.
numbers1 = "234,56,123,5785,34,1"
num = numbers1.split(',')
print(num)

number2 = ['2', '3', '4', ' '
                          '4', '5', '1', ' '
                                         '2', '3', '5', ' '
           ]
# Lets join the list together, but with ' ' separator
num2 = ''.join(number2)
print(num2)

# Now lets split it again whenever we see a ' ' and store it in a new list
values = num2.split()
print(values)
