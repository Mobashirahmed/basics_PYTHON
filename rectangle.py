# A Program that takes the length and breadth of a rectangle as input and outputs the area and perimeter of the rectangle.
# Obtaining the length and the breadth of the rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
# Calculating the perimeter of the rectangle
perimeter = 2 * (length + breadth)
print("The perimeter of the rectangle is: ", perimeter)
# Calculating the area of the rectangle
area = length * breadth
print("The area of the rectangle is: ", area)