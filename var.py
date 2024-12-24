a = 10
b = 10
c = 20
# In Python we've memory is alloted for each unique value stored in a variable, but those variable names can be same or different for a givent constant value.
print(a, b, c)
print(id(a), id(b), id(c))
# storing a string in a variable
s = "Chaudhary Devi Lal University"
print(s)
# We should not use any special characters or numbers at the start of a variable name
r1 = 3.14
print(r1)
# Boolean values in Python
_tru= 20 > 10
_fal = 10 > 20
print(_tru, _fal)
# To check the type of a variable we can use type() function
print(type(a), type(s), type(r1), type(_tru))