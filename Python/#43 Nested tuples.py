# Let's take the previous land example and solve for multiple plots of land
# If we use nested tuples, that is tuples in a tuple, we won't be able to change anything in this.

# What if we wanted to add another plot of land which later became available.
# In that case then we will need to add another entry, for that mutable data type is required, hence best is to do
# it inside a list

# tuples inside a bigger list changes this problem


land = [('Delhi', 12, 100.0, 150.0),
        ('Gudgaon', 20, 120.0, 50.0),
        ('Gaziabaad', 25, 50.0, 250.0),
        ('Noida', 15, 10.0, 150.0),
        ('Faridabad', 10, 200.0, 200.0),
        ]
# We can add more plots but we will also not be able to change the attributes of the individual element, which is what
# we want


