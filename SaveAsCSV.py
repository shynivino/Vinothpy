from tkinter import Tk
import tkinter.filedialog as filedialog
import glob,re,csv
import os
import pyautogui as PG
class GenerateCSV:
    count=0
    def choosedir(self):
        choosed=filedialog.askdirectory(title='Please select the Source folder')
        files=self.takefiles(choosed)
        GenerateCSV.count=len(files)
        Updated = filedialog.askdirectory(title='Please select the Destination folder')
        for file in files:
            if re.search("SJR",file):
                self.WriteHeading(file,Updated)
            else:
                name=file.split("\\")
                os.rename(choosed+"\\" + name[-1],choosed+"\\"+"SJR_"+name[-1])
                self.WriteHeading(file,Updated)

    def takefiles(self,choosed):
        return (glob.glob(choosed+"/*.csv"))
    def WriteHeading(self,file,Updated):
        data = []
        name = file.split("\\")

        Updated = Updated+"/"+name[-1]
        with open (file,'r') as f:
            Reader= csv.reader(f)
            count = 0
            for line in Reader:
                if count > 0:
                    data.append(line)
                count+=1

        with open (Updated, 'w',newline='') as f1:
            writer = csv.writer(f1,delimiter=',')
            dat = ['Joint Name','Cable','Seg','Fibre','Fibre','Seg','Cable']
            writer.writerow(dat)
            for i in range(0,len(data)):
                writer.writerow(data[i])

if __name__ == '__main__':
    Tk().withdraw()
    gen= GenerateCSV()
    gen.choosedir()
    PG.alert(text=str(GenerateCSV.count)+' Files Saved as CSV', title='Success')
