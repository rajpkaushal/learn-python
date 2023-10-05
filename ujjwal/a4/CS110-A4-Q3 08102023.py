# print("Write a program in C to input the basic salary of an employee and calculate his/her gross salary according to the following rules:")
# print("i. If basic salary is up to 30000 rupees, he/she gets 20% HRA and 30% DA.")
# print("ii. If basic salary is up to 60000 rupees but more than 30000 rupees, he/she gets 25% HRA and 35% DA.")
# print("iii. If the basic salary is more than 60000 rupees, he/she gets 30% HRA and 40% DA.")
n = input("Name of the Employee: ")
s = int(input("Enter the Basic Salary of Employee: "))
if s <= 30000:
  hra =  s * 0.20
  da = s * 0.30
  print(n, "Basic salary - ", s, "HRA - ", hra, "DA - ", da, "Total Salary = ", s+hra+da )
elif  s <= 60000:
  hra =  s * 0.25
  da = s * 0.35
  print(n, "Basic salary - ", s, "HRA - ", hra, "DA - ", da, "Total Salary = ", s+hra+da )
else: 
  hra =  s * 0.30
  da = s * 0.40
  print(n, "Basic salary - ", s, "HRA - ", hra, "DA - ", da, "Total Salary = ", s+hra+da )