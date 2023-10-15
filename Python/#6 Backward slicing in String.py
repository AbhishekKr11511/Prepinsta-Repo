# We learn the reverse slicing in this module
#            01234567890123456789012345  -> there are 26 alphabets
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets[::-1])  # Easy way to print the string backwards
print(alphabets[25::-1]) # Same result
print(alphabets[-1::-1]) # Same result
print(alphabets[:0:-1]) # This will only exclude the 0th index element that is "a"
print(alphabets[::-2])  # Same but skipping a letter
print(alphabets[-1:4:-1])   # Here this will print from the last element to the 5th element that is "f"

# All rules apply the same way

# print -> onm and nkhe
print(alphabets[14:11:-1])
print(alphabets[13:3:-3])
# print last 20 elements in reverse
print(alphabets[:-21:-1])