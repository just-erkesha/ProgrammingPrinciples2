from math import tan, pi

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
A = int(sides * (length ** 2) / (4 * tan(pi / sides)))
print("The area of the polygon is: ",A)
