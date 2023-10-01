#Write a program that takes an integer x as input and prints the smallest even number larger than x. In other words, if x is even, the output is (x + 2) and (x + 1) otherwise
x = int(input("Please input thr number: "))
if x % 2 == 0:
  print("Next even number is", x + 2)
else:
  print("Next even number is", x + 1)