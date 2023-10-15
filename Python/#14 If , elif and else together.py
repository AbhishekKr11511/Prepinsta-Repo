# Let's use the same problem from #13, to see if the person can vote or not\
# PS:- Don't take offence on the print statements, Just something I do for making programming fun
import sys
name = (input("Enter your name : "))
age = int(input("Enter your age : "))

print(age)

if age < 0 :
    print("Enter a valid age Einstein")
    sys.exit(0)     # We will learn more on this, just know this works like return 0 in C.
elif age < 18 :
    print(f"You are are a kid , Get a job you little ... {age} year'ol bih")
elif age > 100 :
    print("Time for your meds grandpa")
else:
    print("You can vote but don't get political")