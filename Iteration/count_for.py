# Program to print counting numbers upto n using for loop.

n = int(input("Enter the value of n: "))
if n > 0:
    print("Counting numbers upto", n, ": ")
    
    for count in range(1, n+1):
        print(count)
else:
    print("Please! enter a positive number.")