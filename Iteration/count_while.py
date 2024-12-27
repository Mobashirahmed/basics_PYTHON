# Program to print counting number upto n using while loop.

n = int(input("Enter the value of n: "))
count = 1
if n > 0:
    print("Counting numbers upto", n, ": ")
    
    while count <= n:
        print(count)
        count += 1
else:
    print("Please! enter a positive number.")