limit = int(input("Enter the number : "))
i = 0
while i < limit:
    if i % 5 == 0:
        print("The value of i is {0}".format(i))
        #   i = i + 1
        i += i + 1
        continue
    else:
        i += 1
        continue
# run a debugger to check the iteration.
