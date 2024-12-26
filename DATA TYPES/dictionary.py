dictionary = {
    'name' : 'Mobashir',
    'age' : 20,
    'is_student' : True,
    'marks' : [18, 18, 19, 20, 17],
}

print(dictionary, "is of type", type(dictionary))

# Accessing elements of dictionary using keys
print("Name:", dictionary['name'])
print("Age:", dictionary['age'])
print("Marks:", dictionary['marks'])

# Adding new key-value pair
dictionary ['State'] = 'Bihar',
dictionary ['District'] = 'Muzaffarpur'

print(dictionary)