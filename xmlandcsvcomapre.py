designation=[]
def printtext():
    global e
    designation.append(e.get())
    print designation[0]
    root.destroy()

from Tkinter import *
root = Tk()

root.title('Enter Feed_Designation Name')

e = Entry(root,width=36,font=30)
e.pack()
e.focus_set()

b = Button(root,text='Submit',command=printtext,width=20)
b.pack(side='bottom')
root.mainloop()

from xml.etree.ElementTree import parse, Element
import xml.etree.ElementTree as ET
import re, os
from Tkinter import *
import Tkinter
import tkFileDialog
import csv

ET.register_namespace('gml', 'http://www.opengis.net/gml')
ET.register_namespace('nbn', 'http://www.telstra.com.au/nbn')
namespace1 = {'nbn': 'http://www.telstra.com.au/nbn'}
namespace2 = {'gml': 'http://www.opengis.net/gml'}
nsmap = {'nbn': 'http://www.telstra.com.au/nbn', 'gml': 'http://www.opengis.net/gml'}

Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.askopenfilename(title = "Choose your gml file")  # askopenfilename() #Ask to Open a File
file_path, file_name = os.path.split(filename)

tlsid = []
exceltlsid = []
compare = []


try:
    tree = ET.parse(filename)
    root = tree.getroot() 

    for node1 in root.findall('.//gml:featureMember/nbn:copperCable', nsmap):
        tls=node1.find('nbn:tlsID', namespace1)
        feeddesig=node1.find('.//nbn:feedDesignation', namespace1)
        if feeddesig is not None:
            if (feeddesig.text) == designation[0]:                
                tlsid.append(str(tls.text))
    print (tlsid,len(tlsid))
    Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename1 = tkFileDialog.askopenfilename(title = "Choose your excel file")  # askopenfilename() #Ask to Open a File
    file_path, file_name = os.path.split(filename1)
    with open(filename1, 'r') as csvfile:
        count=0
        fieldnames = ['Network Key', 'Cable Name', 'Alternate Name', 'Cable Type', 'Fiber Design Profile', 'Buffer Size', 'Cable Design Length',
                      'Slack Length', 'Cable Asbuilt Length', 'Model Length', 'Cable Strand Length', 'Aerial Length', 'Underground Length',
                      'Buried Length', 'Storage Length', 'Pigtail Length', 'Other Length', 'Sheath Reading at Start', 'Sheath Reading at End',
                      'Installation Date', 'Account Code', 'Miscellaneous Text', 'CLFI Code', 'Plant Owner', 'Reel ID', 'Start Node', 'End Node',
                      'Start Connection', 'End Connection', 'Attribute 1', 'Attribute 2', 'Attribute 3', 'Attribute 4', 'Original Pair Count',
                      'Gauge Diameter', 'Attribute 7', 'Attribute 8', 'Attribute 9', 'Attribute 10', 'Sheath Type', 'Core Construction Type',
                      'Attribute 13', 'Attribute 14', 'Attribute 15', 'Attribute 16', 'Attribute 17', 'Attribute 18', 'Attribute 19', 'Attribute 20',
                      'Attribute 21', 'Attribute 22', 'Attribute 23', 'Attribute 24', 'Attribute 25', 'Attribute 26', 'Attribute 27', 'Attribute 28',
                      'Attribute 29', 'Attribute 30', 'Attribute 31', 'Attribute 32', 'Attribute 33', 'Attribute 34', 'Attribute 35', 'Attribute 36',
                      'Attribute 37', 'Attribute 38', 'Attribute 39', 'Attribute 40','Attribute 41', 'Attribute 42', 'Attribute 43', 'Attribute 44',
                      'Attribute 45', 'Attribute 46', 'Attribute 47', 'Attribute 48', 'Attribute 49', 'Attribute 50', 'Network Key', 'Class Name'] 
        Reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for line in Reader:
            exceltlsid.append((line['Cable Name']).zfill(18))
        print (exceltlsid,len(exceltlsid))
        for i in range(len(tlsid)):
                if tlsid[i] not in exceltlsid:
                    compare.append(tlsid[i])
        print(compare,len(compare))
        compare=list(set(compare))
        print(compare,len(compare))
        missingid="Missig ID's"
        with open(file_path+'\output.csv', 'wb') as csvFile:  # create the consolidation file
            writer = csv.writer(csvFile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(missingid.split())
            for i in range(len(compare)):
                writer.writerow(str(compare[i]).split())       
    
            
    
except OSError as err:
    print("OS ERROR: {0}".format(err))

