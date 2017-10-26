from xml.etree.ElementTree import parse,Element
import xml.etree.ElementTree as ET
import re,os,csv
import Tkinter 
import tkFileDialog

PIT_DUCT_ID=[]
FailedPitDuctID=[]
marked_for_remediate=[]
remediate_duct_yes=[]
notinfirst=[]
notinfirstandsecond=[]
filepath=[]

def gmlparse():
        ET.register_namespace('gml','http://www.opengis.net/gml/3.2')
        ET.register_namespace('nbn','http://www.nbnco.com.au/nbn')
        ET.register_namespace('gml','http://www.opengis.net/gml')
        ET.register_namespace('nbn','http://www.telstra.com.au/nbn')
        
        namespace1={'nbn':'http://www.nbnco.com.au/nbn'}
        namespace2={'gml':'http://www.opengis.net/gml/3.2'}
        nsmap1={'nbn':'http://www.nbnco.com.au/nbn','gml':'http://www.opengis.net/gml/3.2'}
        
        namespace3={'nbn':'http://www.telstra.com.au/nbn'}
        namespace4={'gml':'http://www.opengis.net/gml'}
        nsmap2={'nbn':'http://www.telstra.com.au/nbn','gml':'http://www.opengis.net/gml'}

        
        Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        try:
                filename1 = tkFileDialog.askopenfilename(title="Choose Telstar Network GML File")#askopenfilename() #Ask to Open a 1st File
                filename2 = tkFileDialog.askopenfilename(title="Choose N50 GML File")#askopenfilename() #Ask to Open a 2nd File
                
                file_path1, file_name1 = os.path.split(filename1)
                filepath.append(file_path1)
                file_path2, file_name2 = os.path.split(filename2)

                '''Start finding ID's which having remediation status start with 'M' or 'R' from Telstra network GML file'''
                tree=ET.parse(filename1)   
                root = tree.getroot()     
                
                for node in root.findall('.//gml:featureMember/nbn:supportStructure',nsmap1):
                        nbnid = node.find('.//nbn:tlsID',namespace1)
                        nbnremediate = node.find('.//nbn:remediationStatus',namespace1)
                        if nbnremediate is not None and nbnid is not None:
                                if (nbnremediate.text).startswith("M") or (nbnremediate.text).startswith("R"):
                                        PIT_DUCT_ID.append(nbnid.text)                                
                print("Pit ID's Count:",len(PIT_DUCT_ID))
                print(PIT_DUCT_ID)
                
                for node in root.findall('.//gml:featureMember/nbn:duct',nsmap1):
                        nbnid = node.find('.//nbn:tlsID',namespace1)
                        nbnremediate = node.find('.//nbn:remediationStatus',namespace1)
                        if nbnremediate is not None and nbnid is not None:
                                if (nbnremediate.text).startswith("M") or (nbnremediate.text).startswith("R"):
                                        PIT_DUCT_ID.append(nbnid.text)
                print("Pit and Duct ID's Count:",len(PIT_DUCT_ID))
                print(PIT_DUCT_ID)
                
                '''Start compare remdiation status or remediateDuct of ID's which having remediation status start with 'M' or 'R' in Telstra network GML file with N50 GML file'''
                tree1=ET.parse(filename2)   
                root1 = tree1.getroot()
                for pitductid in PIT_DUCT_ID:
                        for node1 in root1.findall('.//gml:featureMember/nbn:structurePoint',nsmap2):
                                nbnid=node1.find('nbn:tlsID',namespace3)
                                nbnremediate=node1.find('nbn:remediationStatus',nsmap2)
                                if nbnid is not None and nbnremediate is not None:
                                        if pitductid==nbnid.text:
                                                if nbnremediate.text=="Marked for Remediation":                                      
                                                        marked_for_remediate.append(nbnid.text)
                                                        break

                for pitductid in PIT_DUCT_ID:
                        if pitductid not in marked_for_remediate:
                                notinfirst.append(pitductid)
                print("Count of ID's not ""Marked for Remediation:""",len(notinfirst))
                print(notinfirst)

                for pitductid in notinfirst:
                        for node1 in root1.findall('.//gml:featureMember/nbn:remediationDuct',nsmap2):                        
                                nbnid=node1.find('nbn:tlsID',namespace3)
                                nbnremediate=node1.find('nbn:remediateDuct',nsmap2)
                                if nbnid is not None and nbnremediate is not None:                               
                                        if pitductid==nbnid.text:
                                                if nbnremediate.text=="Y":                                      
                                                        remediate_duct_yes.append(nbnid.text)
                                                        break
                                
                for pitductid in PIT_DUCT_ID:
                        if pitductid not in marked_for_remediate and pitductid not in remediate_duct_yes :
                                notinfirstandsecond.append(pitductid)
                print("Count of ID's Not marked ""Marked for Remediation"" and ""nbn:remediateDuct-Y:""",len(notinfirstandsecond))
                print(notinfirstandsecond)

                writereport()#writes report
                
        except IOError as e:
                print("Files Not choosen:",e)
                                
def writereport():
        ''' writes all ID's which failed into Report.csv file'''
        header="FAILED ID's"
        with open(filepath[0]+'/Report.csv', 'wb') as f:
                writer1 = csv.writer(f,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer1.writerow(header.split())
                for pitductid in notinfirstandsecond:
                        writer1.writerow((str(pitductid)).split())
        print("Completed Succesfully and saved Report.csv file in the same path where telstra network GML resided.")

if __name__=='__main__':
    gmlparse()
    
