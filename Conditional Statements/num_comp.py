# Program to tell the greatest of three numbers, entered by the user.

num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
num3 = int (input("Enter the third number: "))

if num1 > num2:
    if num1 > num3:
        print(num1, "is the greatest.")
if num2 > num1:
    if num2 > num3:
        print(num2, "is the greatest.")
if num3 > num1:
    if num3 > num2:
        print(num3, "is the greatest.")
