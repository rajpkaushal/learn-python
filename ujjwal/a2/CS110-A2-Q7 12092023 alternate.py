print("Write a program to reverse a five-digit positive integer. For instance, if the number is 13257, the output needs to be 75231. Do not use any loop construct")
a = input(" Please enter the number or word: ")
l = len(a)
n = l
while n != 0:
 n -= 1
 print(a[n], end="")