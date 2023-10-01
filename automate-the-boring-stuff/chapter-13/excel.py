import openpyxl as xl
wb = xl.load_workbook("example.xlsx")
print(type(wb))
print(wb.sheetnames)
print(wb.active)
sheet = wb.active
cell = sheet["b4"]
print(cell.row)
print(cell.column)
print(cell.value)
cells = sheet["c1":"c7"]
print(cells)
for i in cells:
    print(i.value)
    
    
print("something")