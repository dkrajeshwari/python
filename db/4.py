from openpyxl import Workbook
import csv
with open("as.csv") as file:
    data=csv.reader(file)
wb=Workbook()
sheet=wb.active

for row in data:
    sheet.append(row)
wb.server("ws.xlsx")    
   



