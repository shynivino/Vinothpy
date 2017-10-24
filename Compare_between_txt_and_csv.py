import re,os
from Tkinter import *  #Python 2X
import Tkinter  #Python 2X
import tkFileDialog #Python 2X
import csv,glob
cupid_text=[]
cupid_excel=[]
cupid_match=[]

Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing #Python 2X
choosed=tkFileDialog.askdirectory(title='Please select the Source folder') #askopenfilename() #Ask to Open a File #Python 2X
csvfiles=glob.glob(choosed+"/*.csv")
#print (txtfiles,len(txtfiles))
for file1 in csvfiles:
    with open (file1,'r') as f:
                Reader= csv.reader(f)
                for line in Reader:
                    cupid_excel.append(line[2])
print cupid_excel
txtfiles=glob.glob(choosed+"/*.txt")


for file1 in range(len(txtfiles)-9):
    file = open(txtfiles[file1], "r")
    num_lines = sum(1 for line in open(txtfiles[file1]))
    print (num_lines,"-No of Lines in Text File")
    for i in range(num_lines):
        cupid=(file.readline().split()[-1])
        if cupid != "":
            cupid_text.append(cupid)
    print(len(cupid_text),"-No of CUP ID's from text file")
    
    for i in range(len(cupid_excel)):
        if cupid_excel[i] in cupid_text:
            cupid_match.append(cupid_excel[i])
    print("Len ",len(cupid_match),"No of Matched CUP ID's")


    with open('C:\NPAM\Book2.csv', 'ab') as f: # output csv file
        writer = csv.writer(f)
        writer.writerow("")
        writer.writerow((txtfiles[file1]).split())
        for i in range(len(cupid_match)):
            writer.writerow((cupid_match[i]).split())
