from tkinter import Tk
import tkinter.filedialog as filedialog
import glob, re, csv
import os
from shutil import copyfile
import pyautogui as PG


class GenerateCSV:
    count = 0
    def choosedir(self):
        choosed = filedialog.askdirectory(title='Please select the Source folder')
        files = self.takefiles(choosed)
        GenerateCSV.count = len(files)
        print(files)
        Updated = filedialog.askdirectory(title='Please select the Destination folder')
        Updated=Updated+"/"
        for file in files:
            file1=file.split("\\")
            print(file1[-1],"huli")
            Updated=Updated + str(file1[-1])
            copyfile(file, Updated)

    def takefiles(self, choosed):
        return (glob.glob(choosed + "/*.*"))


if __name__ == '__main__':
    Tk().withdraw()
    gen = GenerateCSV()
    gen.choosedir()
    PG.alert(text=str(GenerateCSV.count) + ' Files Copied Successfully', title='Success')
