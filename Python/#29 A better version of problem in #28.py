# Let's say are like 1000s of items in stock, printing every thing will be tedious, So we can use for loop insteed.
# Made this by myself, much better than the previous one. less go

stock = ['butter',
         'bread',
         'milk',
         'coffee',
         'biscuits',
         'yogurt',
         'cream']
# choice is the made for corresponding value of elements in stock list.
choice = ['1','2','3','4','5','6','7']
# We will see a much better version of this in the next program.

# Print the items in stock list.
print("Add items from the following available items")
for i in range(len(stock)):
    print(f"{i+1}. {stock[i]}")
print('0. Exit')


input_no = input("Enter serial no. of item : ")

# Initialise the shopping cart
grocery_item = []

# We run the loop here infinitely until user decides to break out. Hence, elif statement.
while input_no:
    if input_no in choice and input_no != '0':
        grocery_item.append(stock[int(input_no)-1])
        print(f"{stock[int(input_no)-1]} has been added")
        input_no = input("Enter serial no. of item : ")

    elif input_no == '0':
        print("\nHere's your cart:")
        break

    else:
        print("Enter are valid input :")
        input_no = input("Enter serial no. of item : ")


print(grocery_item)
print("Thanks for shopping with us !!")

