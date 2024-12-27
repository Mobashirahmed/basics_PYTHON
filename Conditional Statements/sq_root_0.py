# A Program to find the square root of a number.

num = int(input("Enter a number: "))
if num >= 0:
    sq_root = num ** 0.5
    print("The square root of", num, "is", sq_root)
else:
    print("You have entered an invalid number.")