n = int(input("Number: "))
a = n%10
a1 = n//10
b = a1%10
b1 = a1//10
c = b1%10
c1 = b1//10
d = c1%10
d1 = c1//10
e = d1%10
s=a*10000+b*1000+c*100+d*10+e
print(s)