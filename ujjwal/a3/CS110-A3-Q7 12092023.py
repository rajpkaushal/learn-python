#Write a program in C to find if a year is a leap year. If it is a leap year, print Y Otherwise, print N
x = int(input("Please Year to Check: "))
if x % 400 == 0:
  print("Y")
elif x % 100 == 0:
  print("N")
elif x % 4 == 0:
  print("Y")
else:
  print("N")