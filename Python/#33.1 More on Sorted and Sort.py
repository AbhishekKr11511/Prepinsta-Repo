list1 = [ 'Mike',
          'Chris',
          'eric',
          'Andy',
          'chloe',
          'Joe']

list1.sort()
print(list1)

# The above code sort the strings based on the ascii value of the 1st character, then 2nd, then 3rd and so on.
# Since Capital letters have a lower ascii value they are printed first.
print()
list2 = [ 'Mike',
          'Chris',
          'eric',
          'Andy',
          'chloe',
          'Joe']

result = sorted(list2)
print(result)

# Same process, different approach
#----------------------------------------------------------------------------------------
# Using case-fold.
print()
list3 = [ 'Mike',
          'Chris',
          'eric',
          'Andy',
          'chloe',
          'Joe']

list3.sort(key=str.casefold) # This will ignore if the characters are uppercase or lowercase
print(list3)
#----------------------------------------------------------------------------------------

print()
list4 = [ 'Mike',
          'Chris',
          'eric',
          'Andy',
          'chloe',
          'Joe']

result = sorted(list4, key=str.casefold)    # Here sorted() takes the parameter as well
print(result)


