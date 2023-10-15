# Write a program to add items to cart from a grocery app, by using using integer inputs
# And take 0 to stop adding items and finalize the order


# We create an empty list


choice = ""
grocery_item = []

while choice != '0':
    if choice in '123456':
        print("Added {0} to big basket cart : ".format(choice))
        if choice == '1':
            grocery_item.append('butter')
        elif choice == '2':
            grocery_item.append('bread')
        elif choice == '3':
            grocery_item.append('milk')
        elif choice == '4':
            grocery_item.append('coffee')
        elif choice == '5':
            grocery_item.append('biscuits')
        elif choice == '6':
            grocery_item.append('yogurt')
        else:
            print("Add items from the following available items")
            print('1. Butter')
            print('2. Bread')
            print('3. Milk')
            print('4. Coffee')
            print('5. Biscuits')
            print('6. Yogurt')
            print('0. Exit')

    choice = input('Enter serial no. : ')

print("Here's your items in cart :\n", grocery_item)

