a = input('please input the number =  ')
b = len(a)
l = b//2
x=a[0:l]
y=a[(-l):]
z=''.join(list(reversed (y))) 
if x==z:
 print( a, "is a palindrome" )
else:
  print( a, "is not a palindrome")