# Write a program to check whether a number is divisible only by either of 7 and 13 (but not both), or not
n = int(input("Please enter the number: "))
a = 7
b = 13
if n % a == 0: 
  print("Given number is divisible with 7 ")
elif  n % b == 0:
  print("Given number is divisible with 13 ")
else:
 print("Given number is not divisible with both 7 & 13")