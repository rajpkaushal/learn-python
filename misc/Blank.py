print("Write a program to check whether a triangle is an equilateral, isosceles, or scalene triangle. Consider all sides of the triangles as inputs.")
print(" ")
a = int(input("input the length of First side of triangle: "))
b = int(input("input the length of Second side of triangle: "))
c = int(input("input the length of third side of triangle: "))
if a == b == c: 
 print("it is an equilateral triangle")
elif a == b:
 print("it is an isosceles triangle")
elif a == c:
 print("it is an isosceles triangle")
elif b == c:
 print("it is an isosceles triangle")
else:
 print("it is a scalene triangle")