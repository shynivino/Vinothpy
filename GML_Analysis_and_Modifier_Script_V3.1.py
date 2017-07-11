from xml.etree.ElementTree import parse,Element
import xml.etree.ElementTree as ET
import re,os
from Tkinter import *
import Tkinter
import tkFileDialog
import csv

ET.register_namespace('gml','http://www.opengis.net/gml')
ET.register_namespace('nbn','http://www.telstra.com.au/nbn')
namespace1={'nbn':'http://www.telstra.com.au/nbn'}
namespace2={'gml':'http://www.opengis.net/gml'}
nsmap={'nbn':'http://www.telstra.com.au/nbn','gml':'http://www.opengis.net/gml'}

Tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.askopenfilename() #askopenfilename() #Ask to Open a File
file_path, file_name = os.path.split(filename)

ccu=[]
ccutype=[]
struct_id=[]
ccu_joint=[]
stid1=[]
missed_Joint=[]
StructurepointID=[]
missed_SP=[]
stpoint=[]
ccu_id=[]
co_ordinates=[]
NEC_002=[]
hv_lv_nbn_id=[]
fnoneci=[]
Virtual_node_nbn_id=[]
fno_structurepoint=[]
var1 = StringVar()
fuseid=[]
fttbid=[]
fttbtemp=[]
FTTB=[]
css=[]

def indent(elem, level=0):
    ''' indeting GML File Content ''' 
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def Add_StructurePoint(strucP_id,co_ordinate):
    '''Adding -CCU-00 structurePoint to gml:featureMember'''
    StructurePoint=ET.Element("gml:featureMember")
    ct=ET.SubElement(StructurePoint,"nbn:structurePoint")
    ET.SubElement(ct,"nbn:id").text=strucP_id
    ET.SubElement(ct,"nbn:structurePointType").text="CCU"
    ET.SubElement(ct,"nbn:type").text="Pillar"
    ET.SubElement(ct,"nbn:size").text='1800'
    ET.SubElement(ct,"nbn:constructionStatus").text='Planned'
    ET.SubElement(ct,"nbn:owner").text="NBN Co"
    ET.SubElement(ct,"nbn:indicativePitOccupancy").text='N/A'
    ET.SubElement(ct,"nbn:targetAssetFlag").text='N'
    ct1=ET.SubElement(ct,"gml:pointProperty")
    ct2=ET.SubElement(ct1,"gml:Point", srsName="EPSG:4283",srsDimension="2")
    ET.SubElement(ct2,"gml:pos").text=co_ordinate

    for node in root.findall('.//gml:FeatureCollection',namespace2):
        '''Loop through all gml:Feature Collection'''
    node.append(StructurePoint)

def Add_Joint(jointid,stid1):
    '''Adding -CCU-00 joint to gml:featureMember'''
    Joint=ET.Element("gml:featureMember")
    ct=ET.SubElement(Joint,"nbn:joint")
    ET.SubElement(ct,"nbn:id").text=jointid
    ET.SubElement(ct,"nbn:jointType").text="Copper"
    ET.SubElement(ct,"nbn:specification").text="Unknown Unknown"   
    ET.SubElement(ct,"nbn:constructionStatus").text='Built-Installed'
    ET.SubElement(ct,"nbn:owner").text="Telstra"
    ET.SubElement(ct,"nbn:structurePointId").text=stid1 #(re.sub('CCU','NEC',jointid))#[:11])+'NEC-002'
    ET.SubElement(ct,"nbn:targetAssetFlag").text='Y'
    ET.SubElement(ct,"nbn:networkBoundaryPointFlag").text='N'

    for node in root.findall('.//gml:FeatureCollection',namespace2):
        '''Loop through all gml:Feature COllection'''
    node.append(Joint)
def writereport():
    header="List of ID's Having Error"
    with open(file_path+'/'+newFileName+'.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(header.split())
        csvwriter.writerow("")
        csvwriter.writerow(("CCU Error").split())
        for i in set(ccu):
            csvwriter.writerow(i.split())
            
        for i in set(ccutype):
            csvwriter.writerow(i.split())
            
        for i in set(struct_id):
            csvwriter.writerow(i.split())


        csvwriter.writerow("")
        csvwriter.writerow(("CCU Joint Missed").split())
        for i in missed_Joint:
            csvwriter.writerow(i.split())   
        
        csvwriter.writerow("")
        csvwriter.writerow(("StructurePoint Missed").split())            
        for i in missed_SP:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("Trench Error").split())       
        for i in set(ccu_id):
            csvwriter.writerow(i.split())
            
        csvwriter.writerow("")
        csvwriter.writerow(("CCU Structurepoint").split())
        for i in set(NEC_002):
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("Pole Error").split())
        for i in hv_lv_nbn_id:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("FNO Error").split())
        for i in Virtual_node_nbn_id:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("FTTB Conversion").split())      
        for i in set(fttbid):
            csvwriter.writerow(i.split())
        
        csvwriter.writerow("")
        csvwriter.writerow(("Fuse Error").split())
        for i in fuseid:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("CSS Error").split())
        for i in css:
            csvwriter.writerow(i.split())                  
        
        
    print(newFileName+'.csv')
    print('Log File generated Successfully')
    
    

try:
    tree=ET.parse(filename)
    root = tree.getroot()
    
    for node1 in root.findall('.//nbn:header',namespace1):
        sam_name=node1.find('nbn:requestID',namespace1)
        newFileName=sam_name.text[:7]#Get SAM name
        updatedgml=file_path+'/'+newFileName+'.gml'

    for node1 in root.findall('.//gml:featureMember/nbn:ccu',nsmap):
        nbnid = node1.find('nbn:id',namespace1)
        if (re.search('NEC-001',nbnid.text) or re.search('NEC-002',nbnid.text)):
            ccu.append(nbnid.text)
            nbnid.text=str(nbnid.text[:11])+'CCU-001'
        if (re.search('NEC-003',nbnid.text)):
            ccu.append(nbnid.text)
            nbnid.text=str(nbnid.text[:11])+'CCU-002'
            
    for node1 in root.findall('.//gml:featureMember/nbn:ccu',nsmap):
        nbnid = node1.find('nbn:id',namespace1)       
        if (re.search('CCU',(nbnid.text))):
            CCU_type=node1.find('nbn:ccuType',namespace1)
            if CCU_type.text!='CCU':
                ccutype.append(nbnid.text)
                CCU_type.text='CCU'
            
    for node1 in root.findall('.//gml:featureMember/nbn:ccu',nsmap):
        nbnid = node1.find('nbn:id',namespace1)       
        if (re.search('CCU',nbnid.text)):
            strucP_id=node1.find('nbn:structurePointId',namespace1)
            if (re.search('CCU',strucP_id.text)):
                struct_id.append(strucP_id.text)
                strucP_id.text=re.sub('CCU','NEC',strucP_id)

    for node1 in root.findall('.//gml:featureMember/nbn:ccu',nsmap):
        nbnid=node1.find('nbn:id',namespace1)
        nbn=node1.find('nbn:structurePointId',namespace1)
        if(re.search('CCU-00',nbnid.text)):
            ccu_joint.append(nbnid.text)
            StructurepointID.append(nbn.text)

    for ccujoint in ccu_joint:
            flag=1
            for node1 in root.findall('.//gml:featureMember/nbn:joint',nsmap):
                nbnid=node1.find('nbn:id',namespace1)
                if(re.search(ccujoint,nbnid.text)):
                    flag=0
                    break;
            if(flag==1):
               missed_Joint.append(ccujoint)

    for k in range(len(missed_Joint)):
        for node1 in root.findall('.//gml:featureMember/nbn:ccu', nsmap):
            nbnid = node1.find('nbn:id', namespace1)
            stid = node1.find('nbn:structurePointId', namespace1)
            if (re.search(missed_Joint[k], nbnid.text)):
                stid1.append(stid.text)
                break

    for i in range(len(missed_Joint)):
        Add_Joint(missed_Joint[i], stid1[i])

    for i in range(len(StructurepointID)):
        flag=1
        for node1 in root.findall('.//gml:featureMember/nbn:structurePoint',nsmap):
            nbnid=node1.find('nbn:id',namespace1)
            if(re.search(StructurepointID[i],nbnid.text)):
                flag=0
                break;
        if(flag==1):
           missed_SP.append(StructurepointID[i])

    for node1 in root.findall('.//gml:featureMember/nbn:structureRoute',nsmap):
        nbnid=node1.find('nbn:id',namespace1)
        if(re.search('-TRE-',nbnid.text)):
           start=node1.find('nbn:startStructurePointID',namespace1)
           end=node1.find('nbn:endStructurePointID',namespace1)

           if (re.search('CCU',start.text)):
               ccu_id.append(nbnid.text)
               start.text=re.sub('CCU','NEC',(start.text))

           if (re.search('CCU',end.text)):
               ccu_id.append(nbnid.text)
               end.text=re.sub('CCU','NEC',(end.text))

    for i in range(len(missed_SP)):
        for node1 in root.findall('.//gml:featureMember/nbn:structureRoute',nsmap):
            nbnid=node1.find('nbn:id',namespace1)
            if(re.search('-TRE-',nbnid.text)):
               start=node1.find('nbn:startStructurePointID',namespace1)
               end=node1.find('nbn:endStructurePointID',namespace1)
               if (re.search(missed_SP[i],start.text)):
                   co_ordinate=node1.find('.//gml:posList',namespace2)
                   co_ordinate1=(co_ordinate.text).split(' ')
                   co_ordinate1=co_ordinate1[0]+' '+co_ordinate1[1]
                   co_ordinates.append(co_ordinate1)
                   break
               if (re.search(missed_SP[i],end.text)):
                   co_ordinate=node1.find('.//gml:posList',namespace2)
                   co_ordinate1=(co_ordinate.text).split(' ')
                   co_ordinate1=co_ordinate1[len(co_ordinate1)-(len(co_ordinate1)+2)]+' '+co_ordinate1[len(co_ordinate1)-(len(co_ordinate1)+1)]
                   co_ordinates.append(co_ordinate1)
                   break
                
    for i in range(len(missed_SP)):
        Add_StructurePoint(missed_SP[i],co_ordinates[i])
        
    indent(root)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    tree=ET.parse(updatedgml)
    
    root1 = tree.getroot()
    for node1 in root1.findall('.//gml:featureMember/nbn:ccu',nsmap):
        nbnid=node1.find('nbn:id',namespace1)
        nbn=node1.find('nbn:structurePointId',namespace1)
        if(re.search('CCU-00',nbnid.text)):
            StructurepointID.append(nbn.text)

    parent_tag='.//gml:featureMember/nbn:structurePoint'

    for i in range(len(StructurepointID)):
        for node1 in root1.findall(parent_tag,nsmap):
            nbnid = node1.find('nbn:id',namespace1) 
            if (re.search(StructurepointID[i],nbnid.text)):
                nbn_spt=node1.find('nbn:structurePointType',namespace1)
                if((nbn_spt.text) != 'CCU'):
                    NEC_002.append(nbnid.text)
                    nbn_spt.text='CCU'
                    
                nbntype=node1.find('nbn:type',namespace1)
                if((nbntype.text)!= 'Pillar'):
                    NEC_002.append(nbnid.text)
                    nbntype.text = 'Pillar'
                    
                nbnsize=node1.find('nbn:size',namespace1)
                if ((nbnsize.text) == '-'):
                    NEC_002.append(nbnid.text)         
                    nbnsize.text='1800'                               
                break

    for node1 in root1.findall(parent_tag,nsmap):
        nbnid=node1.find('nbn:id',namespace1)
        if (re.search('-POL-',(nbnid.text))):
            nbntype = node1.find('nbn:type',namespace1)
            if (nbntype.text)=='HV/LV' or (nbntype.text)=='HV' or (nbntype.text)=='LV' or (nbntype.text)=='LV/HV' or (nbntype.text)=='Service Pole':
                nbnid=node1.find('nbn:id',namespace1)
                hv_lv_nbn_id.append(nbnid.text)
                nbntype.text='Joint Use'

    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid=node1.find('nbn:id',namespace1)
        jointtype=node1.find('nbn:jointType',namespace1)
        if (re.search('-FNO-',nbnid.text)) and (jointtype.text)!="FTTB" :
            necid=node1.find('nbn:structurePointId',namespace1)
            fnoneci.append(necid.text)

    for i in range(len(fnoneci)):
        for node1 in root1.findall(parent_tag,nsmap):
            nbnid = node1.find('nbn:id',namespace1)
            
            if (re.search(fnoneci[i],nbnid.text)):
                nbntype=node1.find('nbn:type',namespace1)
                if ((nbntype.text!= 'Null Node')):
                    Virtual_node_nbn_id.append(nbnid.text)                    
                    nbntype.text='Null Node'
                    
                nbnsize = node1.find('nbn:size', namespace1)
                if ((nbnsize.text != '-')):
                    Virtual_node_nbn_id.append(nbnid.text)
                    nbnsize.text = '-'
                   
                nbnstructurePointType = node1.find('nbn:structurePointType', namespace1)
                if ((nbnstructurePointType.text != 'Pit/Manhole')):
                    Virtual_node_nbn_id.append(nbnid.text)
                    nbnstructurePointType.text = "Pit/Manhole"
                break
            

    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id', namespace1)
        if (re.search('-FUS-',(nbnid.text))):
            nbnjointType = node1.find('nbn:jointType',namespace1)
            if ((nbnjointType.text) != 'Electrical'):
                nbnjointType.text = 'Electrical'
                fuseid.append(nbnid.text)
            nbnspecification = node1.find('nbn:specification',namespace1)
            if nbnspecification is not None:
                if ((nbnspecification.text) != 'FUS'):
                    nbnspecification.text = 'FUS'
                    fuseid.append(nbnid.text)
            
    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id',namespace1)               
        if (re.search('-FNO-',nbnid.text)):
            jointType=node1.find('nbn:jointType',namespace1)
            if jointType.text=='FTTB':
                fttbid.append(nbnid.text)
                fttbtemp.append(nbnid.text)
                nbnid.text=nbnid.text[:11]+'FBU-1'+nbnid.text[-2:]
                
                

    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id',namespace1)
        if (re.search('-FBU-',nbnid.text)):
            jointType=node1.find('nbn:jointType',namespace1)             
            if jointType.text=="FTTB":
                jointType.text='Fibre'
                specification=node1.find('nbn:specification',namespace1)
                if specification is not None:
                    specification.text='D_TYCO_FIST-GCO2-BD-R12'
                    structurePointId=node1.find('nbn:structurePointId',namespace1)
                    fno_structurepoint.append(structurePointId.text)
                    fttbid.append(nbnid.text)

    for fttb_id in fttbtemp:
        for node1 in root1.findall('.//gml:featureMember/nbn:cable',nsmap):
            nbnid = node1.find('nbn:id',namespace1)               
            if (re.search('-HSD-',nbnid.text)):
                start=node1.find('nbn:cableStartJoint',namespace1)
                end=node1.find('nbn:cableEndJoint',namespace1)
                if start.text==fttb_id:
                    start.text=fttb_id[:11]+'FBU-1'+fttb_id[-2:]
                    break
                if end.text==fttb_id:
                    end.text=fttb_id[:11]+'FBU-1'+fttb_id[-2:]
                    break             
        
                
    for fno_structurepointid in fno_structurepoint:
        for node1 in root1.findall('.//gml:featureMember/nbn:structurePoint',nsmap):
            nbnid = node1.find('nbn:id',namespace1)               
            if (re.search(fno_structurepointid,nbnid.text)):
                nbntype=node1.find('nbn:type',namespace1)
                if nbntype.text=='Null Node':
                    nbntype.text='Manhole-Footway'
                    break
                
    for node1 in root1.findall('.//gml:featureMember/nbn:ductStructureRoute',nsmap):
        nbnid = node1.find('nbn:index',namespace1)               
        if nbnid is None:
            index=ET.Element("nbn:index")
            index.text="1"
            node1.append(index)
            
    for node1 in root1.findall('.//gml:featureMember/nbn:cable',nsmap):
        nbnid = node1.find('nbn:id',namespace1)               
        if (re.search('-CSS-',nbnid.text)):
            specification=node1.find('nbn:specification',namespace1)
            if specification is not None:
                if specification.text=='CU_400_040_CPFUT_PE_CCU_PRYS':
                    specification.text='CU_400_040_CPFUT_PE_PRYS'
                    css.append(nbnid.text)
                    
    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id', namespace1)
        if (re.search('-FNO-',(nbnid.text))):
            specification = node1.find('nbn:specification',namespace1)
            if specification is not None:
                if ((specification.text) == 'FNO_384_COMMSCOPE'):
                    specification.text = 'ISAM_384'
       
    indent(root1)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    writereport()
    print(updatedgml)
    print('GML generated Successfully')

except OSError as err:
    print("OS ERROR: {0}".format(err))
