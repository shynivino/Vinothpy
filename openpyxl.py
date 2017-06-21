import openpyxl
import random
wb=openpyxl.load_workbook(filename=r"C:\Users\b.doddahulugappa\Desktop\Copy of resource list1.xlsx")
ws=wb.worksheets[0]
n=random.randrange(1,20)
ws["A"+str(n)]="HelloWorld"
wb.save(r"C:\Users\b.doddahulugappa\Desktop\Copy of resource list1.xlsx")