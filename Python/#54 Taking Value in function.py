counter = 0
list1 = []
while1 = 1

def getValue(name, counter):
    counter += 1
    print("name added")
    list1.append(name)

while while1 == 1:
    name1 = input('Enter name of student : ')
    getValue(name1, counter)
    while1 = int(input("enter 1 to continue or any button to stop: "))

print(list1)
print(counter)