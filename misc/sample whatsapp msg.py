x = int(input("please input the number: "))
while x!=0:
  n = x%10
  x = x // 10
  print(n, end="")
  