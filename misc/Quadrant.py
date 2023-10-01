X = int(input( "Specify the Value of X: "))
Y = int(input( "Specify the Value of Y: "))
if X>=0 and Y>=0:
  print( "The values fall in Q1")
elif X<0 and Y>=0:
 print( "The values fall in Q2")
elif X<0 and Y<0:
 print( "The values fall in Q3")
elif X>=0 and Y<0:
 print( "The values fall in Q4")
