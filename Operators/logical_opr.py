# Logical Operators are used to combine conditional statements.

x = 10
y = 20

print( x == 10 and x < y) # True
print( x == 10 and x < y and x == y) # False

print( x == 10 or x < y) # True
print( x == 10 or x < y or x == y) # True
print( x != 10 or x < y or x == y) # True
print( x != 10 or x > y or x == y) # False

print(not x != 10) # True