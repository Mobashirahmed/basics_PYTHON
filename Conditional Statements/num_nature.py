# A Program to tell the nature of the number entered by the user.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("You have entered zero.")