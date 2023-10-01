k = int(input("Please input the number:  "))
i = 1
e = 1
while e < k:
  e = 2**i
  i +=1
print(e)
i -=2
f = 2**i
print (f)
x = e - k
y = k - f
if x >= y:
  print (" the nearest value of 2** is ", i, "and Value is", f)
else :
  print (" the nearest value of 2** is ", i+1,  "and Value is", e)
