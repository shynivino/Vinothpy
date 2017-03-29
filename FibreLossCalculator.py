import openpyxl
import csv,re
import pyautogui as PG
from tkinter.filedialog import askopenfilename
from tkinter import Tk



# ----------------------------------------------------------------------
class FibreLossCalculator:
    try:
        def open_file(self,path,SAM_NAME):
            """
            Open and read an Excel file
            """
            book = openpyxl.load_workbook(path)
            sheet = book.get_sheet_by_name('Working')
            sheet1 = book.get_sheet_by_name('L550_FTTN_XXXX_XX_X')
            sheet2= book.get_sheet_by_name('L570_DSS_XXXX_XX_X')
            sheet3 = book.get_sheet_by_name('L571_HSD_XXXX_XX_X')
            sheet4 = book.get_sheet_by_name('L572_DJL_XXXX_XX_X')
            sheet1.title = 'L550_FTTN_'+SAM_NAME+'_1'
            sheet2.title = 'L570_DSS_'+SAM_NAME+'_1'
            sheet3.title = 'L571_HSD_'+SAM_NAME+'_1'
            sheet4.title = 'L572_DJL_'+SAM_NAME+'_1'
            sheet['B1'] = SAM_NAME
            sheet['K1'] = 1
            self.OpenFttn(sheet1)
            self.OpenOpticalCable(sheet2,sheet3)
            self.OpenJoint(sheet4)
            book.save(SAM_NAME+'_Fiber_Loss_Calculator.xlsx')
            PG.alert(text='Please fill the DJL details in the DJL sheet', title='DJL Details')
    except(Exception) as e:
        print(e)

    try:

        def OpenFttn(self,sheet1):
                Tk().withdraw()
                choosed=askopenfilename(title='Please select FTTN File')
                print(choosed,"choosed")
                list = []
                list1 = []
                with open(choosed,'r')as f:
                    Reader = csv.reader(f)
                    count = 0
                    for line in Reader:
                        if count > 0:
                            list.append(line[0])
                            list1.append(line[1])
                        count+=1
                print(list,"infttn")
                self.list1(list,list1,sheet1)
    except(Exception)as e:
        print(e)

    try:

        def list1(self,list,list1,sheet1):
            print("inside the function")
            #for line in range(0,len(list)):
            #    print("list",list[0],list1[0])
            for line1 in range(0,len(list)):
                sheet1['A'+str(line1+2)] = list[line1]
                sheet1['B'+str(line1+2)] = list1[line1]
                sheet1['D'+str(line1+2)] = 'UG'
                sheet1['E'+str(line1+2)] = 'PLANNED'
                sheet1['F'+str(line1+2)] = 0
    except(Exception) as e:
        print(e)
    try:

        def OpenOpticalCable(self,sheet2,sheet3):
            Tk().withdraw()
            choosed1 = askopenfilename(title='Please select Optical Cable File')
            print(choosed1, "choosed")
            list=[]
            list1=[]
            list2=[]
            list3=[]
            list4=[]
            list5=[]
            list6=[]
            list7=[]
            list8=[]
            list9=[]


            with open(choosed1, 'r')as f:
                Reader = csv.reader(f)
                count = 0
                for line in Reader:
                    if re.search('-DSS-',line[0]):
                        #print(line[0],"dss contains")
                        if count > 0:
                            list.append(line[0])
                            list1.append(line[1])
                            list2.append(line[2])
                            list3.append(line[3])
                            list4.append(line[5])
                        count+=1
                    else:
                        if count > 0:
                            list5.append(line[0])
                            list6.append(line[1])
                            list7.append(line[2])
                            list8.append(line[3])
                            list9.append(line[5])
                        count+=1
            self.writedata(sheet2,sheet3,list,list1,list2,list3,list4,list5,list6,list7,list8,list9)
    except(Exception)as e:
        print(e)

    try:

        def writedata(self,sheet2,sheet3,list,list1,list2,list3,list4,list5,list6,list7,list8,list9):
            #print("list",list[0],list1[0])
            print(len(list),list,"printing the length")
            for i in range(0,len(list)):
                sheet2['A'+str(i+2)] = list[i]
                sheet2['B'+str(i+2)] = list1[i]
                sheet2['C'+str(i+2)] = "DSS_CORNING_"+list4[i]+"_RIBBON"
                sheet2['D'+str(i+2)] = 'UG'
                sheet2['E'+str(i+2)] = list2[i]
                sheet2['F'+str(i+2)] = list3[i]
                sheet2['G'+str(i+2)] = 1
                sheet2['H'+str(i+2)] = 'PLANNED'

            for i in range(0,len(list5)):
                sheet3['A'+str(i+2)] = list5[i]
                sheet3['B'+str(i+2)] = list6[i]
                sheet3['C'+str(i+2)] = "DSS_CORNING_"+list9[i]+"_RIBBON"
                sheet3['D'+str(i+2)] = 'UG'
                sheet3['E'+str(i+2)] = list7[i]
                sheet3['F'+str(i+2)] = list8[i]
                sheet3['G'+str(i+2)] = 1
                sheet3['H'+str(i+2)] = 'PLANNED'
    except(Exception)as e:
        print(e)

    try:

        def OpenJoint(self,sheet4):
                Tk().withdraw()
                choosed2=askopenfilename(title='Please select Optical Joint')
                print(choosed2,"choosed")
                list = []
                with open(choosed2,'r')as f:
                    Reader = csv.reader(f)
                    count = 0
                    for line in Reader:
                        if (re.search('-DJL-',line[0])) or (re.search('-ODF-',line[0])):
                            list.append(line[0])
                        count+=1
                print(list,"infttn")
                self.writejoint(list,sheet4)
    except(Exception)as e:
        print(e)
    try:

        def writejoint(self,list,sheet2):
            for i in range(0,len(list)):
                sheet2['A'+str(i+2)] = 0
                sheet2['B'+str(i+2)] = list[i]
                sheet2['C'+str(1+2)] = "D_TYCO_FIST - GCO2 - BC - R12"
                sheet2['C'+str(len(list)-1)] = "D_CORNING_288 -ORS - MB"
                if re.search('-ODF-',list[i]):
                    sheet2['D'+str(i+2)] = 'OT'
                else:
                    sheet2['D'+str(i+2)] = 'UG'
                sheet2['E'+str(i+2)] = "PLANNED"
    except(Exception)as e:
        print(e)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    fibre=FibreLossCalculator()
    Tk().withdraw()
    try:
        path = askopenfilename(title='Please select Fiber_Loss_Calculator file')
        if (path):
            SAM_NAME=PG.prompt(text='Enter SAM Name', title='SAM Name' , default='1ABC_01')
        fibre.open_file(path,SAM_NAME)
    except(Exception)as e:
        print(e)
