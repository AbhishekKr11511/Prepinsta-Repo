# Lets see if a person is able to able to vote or not
age = int(input("Enter your age : "))

# Till now we have seen and / or usage. But we can also write that condition as below
if 18 <= age < 100:
    print("You can vote.")
else:
    print("You can't vote.")

if age >= 18 and age < 100:     # Use of <and>
    print("Please vote.")
else:
    print("Ineligible to vote.")

#---------------------------------------------------------------------------

if age < 18 or age > 70 :       # Use of <or>
    print("ENJOY your life bro!!")
else:
    print("Work is important!!")
print()
#---------------------------------------------------------------------------

car = "Honda"
# We can also see if the substring is present or not in bigger string
if 'Hon' or 'da' in car:    # This yields <True>
    print("lets goo")
else:
    print("!pow!pow!pow!")

car = "Honda"

