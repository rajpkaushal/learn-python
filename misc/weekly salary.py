name = input( "what is your name: ")
work = int(input( "how many hours you worked during week: "))
rate = 100
if work <= 40:
  rs = work*rate
else:
 rs = 40*rate
print("your Regular salary is", rs)
if work <= 40:
  ot = 0
else:
  ot = (work-40)*rate*1.5
print( "Overtime Pay is", ot)
print("Your Total Pay is", rs+ot)
