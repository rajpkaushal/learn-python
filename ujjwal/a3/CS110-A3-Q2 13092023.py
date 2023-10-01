a = int(input("Please enter the number: "))
b = int(input("Please enter the number: "))
c = int(input("Please enter the number: "))
import math
d = max(a, b, c)
print("The Maximum of entered numbers is ", d)

# alternate method

d = 0
if a < b:
  d = b
else:
  d = a
if d < c:
  print(c)
else:
  print(d)
