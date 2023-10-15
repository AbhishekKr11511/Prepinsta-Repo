import math
L = [3, 1, 2, 4]
T = ('A', 'b', 'c', 'd')
L.sort()
counter = 0
for x in T:
    L[counter] += ord(x)
    counter += 1
    break
print(math.ceil(max(L)/min(L)))
'''
t=(9,10,11,1,11)
s=0
for i in t:
    if(t.count(i)>1):
        s+=(i//2)
    else:
        s+=i*(t.index(i))
print(s)
'''
'''
import math

x = [301.16, 400.71, 500.8, 530.71]
s = 0
for i in x:
    s += math.ceil(i)
print(s)
'''
'''
grocery_bag = ['bread', 'butter', 'Unavailable', 'cream','corn', 'Unavailable','Unavailable','Unavailable','Unavailable']

for item in range(len(grocery_bag) - 1, -1, -1):
    if grocery_bag[item] == 'Unavailable':
        grocery_bag.pop(item)
    else:
        continue
print(grocery_bag)

list1=['python','java','c']
list2=[]
for i in list1:
    list2.append(i.capitalize())
print(list2)
'''

'''
#
list1 = []
list1.append([1, [2, 3], 4])
print(list1)
list1.extend([7, 8, 9])
print(list1)
print(list1[0][1][1] + list1[2])

'''
'''
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)
print(len(test)**2)
'''
