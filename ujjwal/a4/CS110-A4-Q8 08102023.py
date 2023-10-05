# Print all Armstrong numbers between 1 to 500
# for x in range (1000001):
#   n = x
#   n1 = str(n)
#   l = len(n1)
#   sum = 0
#   m = 0
#   while n % 10 > 0:
#     m = n%10
#     sum = sum + (m**l)
#     n = n//10
#   if sum == x:
    # print(x, "number is armstrong")
  # else:
  #   print(x, "this number is not armstrong")
  
  # alternate code
  # Print all Armstrong numbers between 1 to 500
for x in range (1000001):
  n = x
  n1 = str(n)
  l = len(n1)
  sum = 0
  m = 0
  for i in range(l):
    m = n%10
    sum = sum + (m**l)
    n = n//10
  if sum == x:
    print(x, "number is armstrong")
  # else:
  #   print(x, "this number is not armstrong")