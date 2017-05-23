from xml.etree.ElementTree import parse,Element
import xml.etree.ElementTree as ET

import re,os,csv
import Tkinter ##Python 2+
import tkFileDialog ##Python 2+
#from tkinter import Tk ##Python 3+
#from tkinter.filedialog import askopenfilename ##Python 3+

locid=[]
nolocid=[]
csvlocid=[]
updatedfile=[]

def gmlediter():
        ET.register_namespace('gml','http://www.opengis.net/gml')
        ET.register_namespace('nbn','http://www.telstra.com.au/nbn')
        namespace1={'nbn':'http://www.telstra.com.au/nbn'}
        namespace2={'gml':'http://www.opengis.net/gml'}
        nsmap={'nbn':'http://www.telstra.com.au/nbn','gml':'http://www.opengis.net/gml'}

        #Python 3+
        #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        #filename = askopenfilename() #Ask to Open a File

        #Python 2+
        Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = tkFileDialog.askopenfilename()#askopenfilename() #Ask to Open a File
        
        file_path, file_name = os.path.split(filename)
        

        
        tree=ET.parse(filename)   
        root = tree.getroot()    
        for node1 in root.findall('.//nbn:header',namespace1):
                sam_name=node1.find('nbn:requestID',namespace1)
                newFileName=sam_name.text[:7]#Get SAM name      
        
        for node1 in root.findall('.//gml:featureMember/nbn:serviceLocation',nsmap):
                nbnid = node1.find('nbn:locID',namespace1)
                if nbnid is not None:
                                if (re.search('LOC',nbnid.text)):
                                                locid.append(nbnid.text)

        updatedfile.append(file_path+'/'+newFileName+'.csv')
        print(updatedfile)
        print(locid)
        print("No of Location ID's present in GML:",len(locid))
        
        
        
def readcsv():
        filename1 = tkFileDialog.askopenfilename()
        with open(filename1, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                                print(row[0])
                                csvlocid.append(row[0])
        print("List of Locations which are in Sheet:",csvlocid)
        print("No of Location ID's present in GML:",len(csvlocid))
        
        print("###################################### Locations Which Are Not Present #######################################")
        for loc in csvlocid:
                if loc not in locid:
                        print(loc)
                        nolocid.append(loc)
        print("No of Locations not there in the sheet:",len(nolocid))
def writecsv():
        with open(updatedfile[0], 'wb') as f:
                writer1 = csv.writer(f,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for loc in nolocid:
                        loc = loc.replace(" ", "")
                        writer1.writerow(loc)

gmlediter()
readcsv()
writecsv()
