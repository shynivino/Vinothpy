"""
Created on Friday April 13 09:15:11 2018

@author: Doddahulugappa : 1011818
"""

import openpyxl
import struct
lines = []
deli = ","
class BoltDetailsDatabase:
    
        def ReadBoltDetailsInputs(self,bolt_input_file):
            self.bolt_input_file = bolt_input_file
            bolt_information = {}
            with open(self.bolt_input_file) as bolt_input:
                bolt_input_file_lines = bolt_input.readlines()
            for line in bolt_input_file_lines:
                if "Read_From_Excel" in line:
                    key, value = line.split("=")
                    bolt_information[key.strip()] = int(value.strip())
            return bolt_information
        
        def launchfrombinary(self,filename):             
            fd_out = open(filename,"rb")
            global lines
            lines = fd_out.readlines() 
            fd_out.close()
        
        def launchfromexcel(self,filename):
            self.filename = filename
            workbook = openpyxl.load_workbook(self.filename)
            worksheet = workbook.get_sheet_by_name("Sheet1")
            fout = open("BoltDetails", 'w')
            
            for i in range(4,12):
                record = []
                for j in range(1,16):
                    record.append(worksheet.cell(row=i,column=j).value) 
                record[0]=str(record[0])
                record[3]=str(record[3])
                entry = struct.pack("{}scdcdc{}scdcdcdcdcdcdcdcdcdcdcd".format(len(record[0]),len(record[3])),record[0],deli,record[1],deli,record[2],deli,record[3],deli,record[4],deli,record[5],deli,record[6],deli,record[7],deli,record[8],deli,record[9],deli,record[10],deli,record[11],deli,record[12],deli,record[13],deli,record[14])
                fout.write(entry + "\n")
                fout.flush()
            fout.close()
            
            with open("BoltDetails", 'rb') as f:
                global lines
                lines = f.readlines()
        
        #adding data to the file
        def AddBoltDetails(self,bolt_name,bolt_NT,bolt_TTY,bolt_TS,bolt_TG,bolt_HAF,bolt_HGN,bolt_HOD,bolt_HBH,bolt_HSD,bolt_BAF,bolt_BGN,bolt_BOD,bolt_BBH,bolt_BSD): 
            fd_out=open('BoltDetails', 'ab') 
            entry=struct.pack("{}scdcdc{}scdcdcdcdcdcdcdcdcdcdcd".format(len(bolt_name),len(bolt_TS)),bolt_name,deli,bolt_NT,deli,bolt_TTY,deli,bolt_TS,deli,bolt_TG,deli,bolt_HAF,deli,bolt_HGN,deli,bolt_HOD,deli,bolt_HBH,deli,bolt_HSD,deli,bolt_BAF,deli,bolt_BGN,deli,bolt_BOD,deli,bolt_BBH,deli,bolt_BSD)            
            global lines
            
            lines.append(entry+"\n")
            fd_out.write(entry+"\n")
            fd_out.flush()
            fd_out.close()
            
        def ModifyBoltDetails(self,bolt_name,bolt_NT,bolt_TTY,bolt_TS,bolt_TG,bolt_HAF,bolt_HGN,bolt_HOD,bolt_HBH,bolt_HSD,bolt_BAF,bolt_BGN,bolt_BOD,bolt_BBH,bolt_BSD): 
            
            
            entry=struct.pack("{}scdcdc{}scdcdcdcdcdcdcdcdcdcdcd".format(len(bolt_name),len(bolt_TS)),bolt_name,deli,bolt_NT,deli,bolt_TTY,deli,bolt_TS,deli,bolt_TG,deli,bolt_HAF,deli,bolt_HGN,deli,bolt_HOD,deli,bolt_HBH,deli,bolt_HSD,deli,bolt_BAF,deli,bolt_BGN,deli,bolt_BOD,deli,bolt_BBH,deli,bolt_BSD)
                  
#            fd_out = open("BoltDetails","rb")   
#            
#            data=[]
#            lines=fd_out.readlines()
#            for line in lines:
#                if bolt_name in line:
#                        continue
#                data.append(line)
#            fd_out.close()
#            fd_out = open("BoltDetails","wb")   
#            for line in data:
#                fd_out.writelines(line)
#            fd_out.writelines(entry+"\n")   
#            fd_out.close()
            
            
            
            global lines
            for line in lines:
                if bolt_name in line: 
                    lines.remove(line)
            lines.append(entry+"\n")
            
            fd_out=open('BoltDetails', 'wb')     
              
            for line in lines:                   
                fd_out.write(line)
                fd_out.flush()
            fd_out.flush()
            
        
        def DeleteBoltDetails(self,bolt_name):
            try:     
#                fd_out = open("BoltDetails","rb")   
#                
#                data=[]
#                lines=fd_out.readlines()
#                for line in lines:
#                    if bolt_name in line:
#                            continue
#                    data.append(line)
#                fd_out.close()
                
                global lines
                for item in lines:
                    if bolt_name in item: 
                        lines.remove(item)
                
                fd_out = open("BoltDetails","wb")   
                for line in lines:
                    fd_out.writelines(line)
                fd_out.close()
                
            except Exception as error:           
                print(error)
    
if __name__ == "__main__":   
    
    
    BoltDetailsDatabaseInstance = BoltDetailsDatabase()
    bolt_information = BoltDetailsDatabaseInstance.ReadBoltDetailsInputs("BoltDetailsInputs.ini")  
    if bolt_information["Read_From_Excel"] == 1:
        filename = "FlangeClearance.xlsx"
        BoltDetailsDatabaseInstance.launchfromexcel(filename)
    else:
        filename = "BoltDetails"
        BoltDetailsDatabaseInstance.launchfrombinary(filename)
        
    n = 1 #this is the initial variable
    while n != 4  :
            print "                 1. Add Bolt Details\n \
                2. Modify Bolt Details\n \
                3. Delete Bolt Details\n \
                4. Exit"
            n = int(raw_input("Enter Your Choice :"))
            
            if n == 1:
                bolt_name = raw_input("Enter the name of the Bolt:")
                bolt_NT = float(raw_input("Enter the bolt_NT of Bolt:"))
                bolt_TTY = float(raw_input("Enter the bolt_TTY of Bolt:"))
                bolt_TS = raw_input("Enter the bolt_TS of Bolt:")
                bolt_TG = float(raw_input("Enter the bolt_TG of Bolt:"))
                bolt_HAF = float(raw_input("Enter the bolt_HAF of Bolt:"))
                bolt_HGN = float(raw_input("Enter the bolt_HGN of Bolt:"))
                bolt_HOD = float(raw_input("Enter the bolt_HOD of Bolt:"))
                bolt_HBH = float(raw_input("Enter the bolt_HBH of Bolt:"))
                bolt_HSD = float(raw_input("Enter the bolt_HSD of Bolt:"))
                bolt_BAF = float(raw_input("Enter the bolt_BAF of Bolt:"))
                bolt_BGN = float(raw_input("Enter the bolt_BGN of Bolt:"))
                bolt_BOD = float(raw_input("Enter the bolt_BOD of Bolt:"))
                bolt_BBH = float(raw_input("Enter the bolt_BBH of Bolt:"))
                bolt_BSD = float(raw_input("Enter the bolt_BSD of Bolt:"))
                BoltDetailsDatabaseInstance.AddBoltDetails(bolt_name,bolt_NT,bolt_TTY,bolt_TS,bolt_TG,bolt_HAF,bolt_HGN,bolt_HOD,bolt_HBH,bolt_HSD,bolt_BAF,bolt_BGN,bolt_BOD,bolt_BBH,bolt_BSD)
                #BoltDetailsDatabaseInstance.AddBoltDetails("M45",23,34,"1.5\"",23,43,45,34,56,77,776,87,97,97,79)
                print "Added ",bolt_name
                
            elif n == 2:
                bolt_name = raw_input("Enter the name of the Bolt:")
                bolt_NT = float(raw_input("Enter the bolt_NT of Bolt:"))
                bolt_TTY = float(raw_input("Enter the bolt_TTY of Bolt:"))
                bolt_TS = raw_input("Enter the bolt_TS of Bolt:")
                bolt_TG = float(raw_input("Enter the bolt_TG of Bolt:"))
                bolt_HAF = float(raw_input("Enter the bolt_HAF of Bolt:"))
                bolt_HGN = float(raw_input("Enter the bolt_HGN of Bolt:"))
                bolt_HOD = float(raw_input("Enter the bolt_HOD of Bolt:"))
                bolt_HBH = float(raw_input("Enter the bolt_HBH of Bolt:"))
                bolt_HSD = float(raw_input("Enter the bolt_HSD of Bolt:"))
                bolt_BAF = float(raw_input("Enter the bolt_BAF of Bolt:"))
                bolt_BGN = float(raw_input("Enter the bolt_BGN of Bolt:"))
                bolt_BOD = float(raw_input("Enter the bolt_BOD of Bolt:"))
                bolt_BBH = float(raw_input("Enter the bolt_BBH of Bolt:"))
                bolt_BSD = float(raw_input("Enter the bolt_BSD of Bolt:"))
                #BoltDetailsDatabaseInstance.ModifyBoltDetails("M36",2300,394,"2.5\"",23,43,45,34,56,77,776,87,97,97,79)
                BoltDetailsDatabaseInstance.ModifyBoltDetails(bolt_name,bolt_NT,bolt_TTY,bolt_TS,bolt_TG,bolt_HAF,bolt_HGN,bolt_HOD,bolt_HBH,bolt_HSD,bolt_BAF,bolt_BGN,bolt_BOD,bolt_BBH,bolt_BSD)
                print "Modified ",bolt_name
                
            elif n == 3:
                 bolt_name = raw_input("Enter the Name of the Bolt:")
                 BoltDetailsDatabaseInstance.DeleteBoltDetails(bolt_name)
                 print "Deleted ",bolt_name
                 
            elif n == 4 :
                pass
            else:
                print "Invalid Option"
    else :
            print("Exited")
