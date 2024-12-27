# A Program to find the square root of a number.
import math
num = int(input("Enter a number: "))
if num >= 0:
    sq_root = math.sqrt(num)
    print(f"The square root of {num} is {sq_root}")
else:
    print("You have entered an invalid number.")