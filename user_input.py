# by defaulyt the input() function returns a string
user_input1 = input("Enter user input1: ")
user_input2 = input("Enter user input2: ")
# print(user_input1)
# print(user_input2)
print (user_input1 + user_input2)

# Type casting
# int() - converts a string to an integer
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Your Sum: ",a + b)

# float() - converts a string to a float
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print("Your Sum: ", a + b)

# eval() - evaluates the string as a python expression
a = eval(input("Enter a number: "))
b = eval(input("Enter another number: "))
print("Your Sum: ", a + b)