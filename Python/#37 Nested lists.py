# Below is a Nested list
grocery_bag = [
    ['bread', 'butter'],
    ['bread', 'butter', 'Unavailable', 'cream'],
    ['bread', 'butter', 'Unavailable', 'cream','corn', 'Unavailable','Unavailable','Unavailable','Unavailable'],
    ['bread', 'butter','cream', 'corn','apple', 'Unavailable','Unavailable','Unavailable'],
    ['bread', 'butter','cream', 'corn','apple', 'Tea bag'],
]

count = 0
for num, item in enumerate(grocery_bag):
    # Only print the list if it doesn't contain "Unavailable".
    if 'Unavailable' not in item:
        print('{0}. -> {1}'.format(num+1 , item))
        for inner_item in item:
            print(inner_item)

    # If 'Unavailable' is found count its number in that list and print that
    else:
        for inner_item in item:
            if inner_item == 'Unavailable':
               count = count +1
        print('List = {0} contains \n{1} <Unavailable> items'.format(item , count))
        count = 0