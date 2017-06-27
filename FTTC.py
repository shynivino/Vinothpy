from xml.etree.ElementTree import parse,Element
import xml.etree.ElementTree as ET
import re,os,csv
import Tkinter 
import tkFileDialog

locid=[]
nolocid=[]
csvlocid=[]
updatedfile=[]

def gmlparse():
        ET.register_namespace('gml','http://www.opengis.net/gml')
        ET.register_namespace('nbn','http://www.telstra.com.au/nbn')
        namespace1={'nbn':'http://www.telstra.com.au/nbn'}
        namespace2={'gml':'http://www.opengis.net/gml'}
        nsmap={'nbn':'http://www.telstra.com.au/nbn','gml':'http://www.opengis.net/gml'}

        
        Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = tkFileDialog.askopenfilename(title="Choose GML File")#askopenfilename() #Ask to Open a File
        
        file_path, file_name = os.path.split(filename)
        

        
        tree=ET.parse(filename)   
        root = tree.getroot()    
        for node1 in root.findall('.//nbn:header',namespace1):
                sam_name=node1.find('nbn:requestID',namespace1)
                newFileName=sam_name.text[:7]#Get SAM name      
        
        for node1 in root.findall('.//gml:featureMember/nbn:serviceLocation',nsmap):
                nbnid = node1.find('nbn:locID',namespace1)
                nbndpChange = node1.find('nbn:dpChange',namespace1)
                if nbnid is not None and nbndpChange is None :
                        #if (re.search('LOC',nbnid.text)):
                        locid.append(nbnid.text)

        updatedfile.append(file_path+'/'+newFileName+'.csv')
        print(updatedfile)
        print(locid)
        print("No of Location ID's present in GML:",len(locid))
        
        
        
def readcsv():
        filename1 = tkFileDialog.askopenfilename(title="Choose CSV File")
        with open(filename1, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                                print(row[0])
                                csvlocid.append(row[0])
        print("List of Locations which are in Sheet:",csvlocid)
        print("No of Location ID's present in GML:",len(csvlocid))
        
        print("###################################### Locations Which Are Not Present #######################################")
        for loc in locid:
                if loc not in csvlocid:
                        print(loc)
                        nolocid.append(loc)
        print("No of Locations not there in the sheet:",len(nolocid))
def writecsv():
        with open(updatedfile[0], 'wb') as f:
                writer1 = csv.writer(f,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for loc in nolocid:
                        writer1.writerow(loc.split())
        print("Script Completed Succesfully")

if __name__=='__main__':
    gmlparse()
    readcsv()
    writecsv()
