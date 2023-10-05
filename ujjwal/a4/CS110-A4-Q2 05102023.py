print("Write a program to check whether a number is Armstrong or not")
x = int(input("enter the number: "))
n = x
n1 = str(n)
l = len(n1)
sum = 0
m = 0
while n % 10 > 0:
    m = n%10
    sum = sum + (m**l)
    n = n//10
if sum == x:
  print(x, "number is armstrong")
else:
  print(x, "this number is not armstrong")


