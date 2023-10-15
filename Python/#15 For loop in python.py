# For loop runs on set of values, which can come from a sequence or iterable object.
# An iterable object can be a String or a list or dictionary or tuple etc
# Range is also an example of iterable. We will work with range in just a moment

message = "good-morning sunshine!!"

for letter in message:  # 'letter' is a variable which will call message as many times as the characters it has.
    print(letter, end="")

print()


for letter in range(len(message)):  # Here we use range() function, Range takes integers as arguments
    # Therefore we use the length of the message, which is an int type as the argument for range.
    print(message[letter], end="")
print()
# Both methods are valid

for letter in range(5, 16,1):    # We can use range function just like we used to slice strings and list
    print(message[letter], end="")


