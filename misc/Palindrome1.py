a = "123454321"
b = len(a)
l = b//2
last = -1
for k in range(l):
  if a[k] == a[last]:
    k =k+1
    last =last-1
  else :
    print (a, "is not a palindrome")
else: 
 print( a, "is a pelindrome")