m = int(input("Enter the marks obtained: "))
if 90 < m < 100:
  print("Grade Obtained - A")
elif 80 < m < 89:
  print("Grade Obtained - B")
elif 70 < m < 79:
  print("Grade Obtained - C")
elif 60 < m < 69:
  print("Grade Obtained - D")
elif 50 < m < 59:
  print("Grade Obtained - E")
elif 40 < m < 49:
  print("Grade Obtained - p")
elif 0 < m < 39:
  print("Grade Obtained - F")
else:
  print("Grade Obtained - X, there is an error in entring the marks")