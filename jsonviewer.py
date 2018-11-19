import json,os,re
import tkinter
from tkinter import Tk,messagebox
from tkinter.filedialog import askdirectory
filename1=[]
Tk().withdraw() # Hide Root window
directory = askdirectory()
dirpath=directory.split('/')
delim='/'
path=delim.join(dirpath)
new_folder=path+'-Updated'
if not os.path.exists(new_folder):
        os.mkdir(new_folder)
else:
    for filename in os.listdir(new_folder):
            full_path = os.path.join(new_folder, filename)
            if os.path.isfile(full_path):
                os.remove(full_path)

for filename in os.listdir(directory):
    if(re.search('.geojson',filename)):
        filename1=(directory+'/'+filename)
        file_path, file_name = os.path.split(filename1)
        with open(filename1) as data_file:
            data = json.load(data_file)
        with open(new_folder+'/'+file_name+'.geojson', 'w') as outfile:
            json.dump(data, outfile,indent = 4,sort_keys=True,separators=(',', ':'))
tkinter.messagebox.showinfo('JSON Files','Modified JSON files and saved in folder named: '+new_folder)
