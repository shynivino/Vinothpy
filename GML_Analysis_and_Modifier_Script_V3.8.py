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
hv_lv_1_nbn_id=[]
hv_lv_2_nbn_id=[]
fnoneci=[]
Virtual_node_nbn_id=[]
fno_structurepoint=[]
var1 = StringVar()
fuseid=[]
fttbid=[]
fttbtemp=[]
FTTB=[]
css=[]
csdfno=[]
jointid1=[]
stid2=[]
telstra_Joint={}
telstra_missed_Joint={}
nbncableID=[]
nbncableID1=[]
countofindex=[]
countofindex1=[]
pcdlist=[]
CIU=[]
csdid=[]
deletedductstructure=[]
deletedccu=[]
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
    '''Adding -CCU- structurePoint to gml:featureMember'''
    StructurePoint=ET.Element("gml:featureMember")
    ct=ET.SubElement(StructurePoint,"nbn:structurePoint")
    ET.SubElement(ct,"nbn:id").text=strucP_id
    ET.SubElement(ct,"nbn:structurePointType").text="CCU"
    ET.SubElement(ct,"nbn:type").text="Pillar"
    ET.SubElement(ct,"nbn:size").text='1800'
    ET.SubElement(ct,"nbn:construction").text="P (Thermoplastic)"
    ET.SubElement(ct,"nbn:constructionStatus").text='Planned'
    ET.SubElement(ct,"nbn:owner").text="NBN Co"
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


def Add_StructureRoute(cable_id,structure_route_id,index_id):
    '''Adding Cable structureRoute to gml:featureMember'''
    StructureRoute=ET.Element("gml:featureMember")
    ct=ET.SubElement(StructureRoute,"nbn:cableStructureRoute")
    ET.SubElement(ct,"nbn:cableID").text=cable_id
    ET.SubElement(ct,"nbn:structureRouteID").text=structure_route_id
    ET.SubElement(ct,"nbn:index").text=index_id

    for node in root.findall('.//gml:FeatureCollection',namespace2):
        '''Loop through all gml:Feature Collection'''
    node.append(StructureRoute)

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

        csvwriter.writerow("")
        csvwriter.writerow(("CSD FNO Designation Changed to ISAM_48").split())
        for i in csdfno:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("Duct Index Added CDS").split())
        csvwriter.writerow(str(len(countofindex)).split())
        
        csvwriter.writerow("")
        csvwriter.writerow(("Trench Index Added CDS").split())
        csvwriter.writerow(str(len(countofindex1)).split())

        csvwriter.writerow("")
        csvwriter.writerow(("PCD SPECS MISSING").split())
        csvwriter.writerow(str(len(pcdlist)).split())

        csvwriter.writerow("")
        csvwriter.writerow(("CIU specification Error").split())
        for i in CIU:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("CSD joint specification Error").split())
        for i in csdid:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("Deleted CCU Block").split())
        for i in deletedccu:
            csvwriter.writerow(i.split())

        csvwriter.writerow("")
        csvwriter.writerow(("Deleted Structureroute Block").split())
        for i in deletedductstructure:
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
            
    cculist=[]
    for node1 in root.findall('.//gml:featureMember/nbn:ccu',nsmap):
        nbnid = node1.find('nbn:id',namespace1)
        if (re.search('CCU',nbnid.text)):
            cculist.append(nbnid.text)
    cculist1=set(cculist)
    cculist1=list(cculist1)
    for i in range(len(cculist1)):
            if cculist.count(cculist1[i]) > 1:
                for node1 in root.findall('gml:FeatureCollection[gml:featureMember]',nsmap):
                    for node2 in node1.findall('gml:featureMember[nbn:ccu]',nsmap):
                        for node3 in node2.findall('nbn:ccu',namespace1):
                            nbnid = node3.find('nbn:id',namespace1)
                            if (re.search(cculist1[i],nbnid.text)):
                                workpack=node3.find('./nbn:workPackage',namespace1)
                                if workpack is None:
                                    node1.remove(node2)
                                    deletedccu.append(cculist1[i])
                                    print("Deleted ",nbnid.text)
                                    break

    ductlist=[]
    for node1 in root.findall('.//gml:featureMember/nbn:ductStructureRoute',nsmap):
        nbnid = node1.find('nbn:ductId',namespace1)
        ductlist.append(nbnid.text)
    ductlist1=set(ductlist)
    ductlist1=list(ductlist1)
    for i in range(len(ductlist1)):
            if ductlist.count(ductlist1[i]) > 1:
                for node1 in root.findall('gml:FeatureCollection[gml:featureMember]',nsmap):
                    for node2 in node1.findall('gml:featureMember[nbn:ductStructureRoute]',nsmap):
                        for node3 in node2.findall('nbn:ductStructureRoute',namespace1):
                            nbnid = node3.find('nbn:ductId',namespace1)
                            if (re.search(ductlist1[i],nbnid.text)):
                                routetype=node3.find('nbn:routeType',namespace1)
                                if routetype.text=="DUCT":
                                    node1.remove(node2)
                                    deletedductstructure.append(ductlist1[i])
                                    print("Deleted ",nbnid.text)
                                    break
    indent(root)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    tree=ET.parse(updatedgml)    
    root = tree.getroot()                        
            
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
        if(re.search('-CCU-',nbnid.text)):
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
               
    missed_Joint=list(set(missed_Joint))
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
        if nbnid is not None:
            if(re.search('-TRE-',nbnid.text)):
               start=node1.find('nbn:startStructurePointID',namespace1)
               end=node1.find('nbn:endStructurePointID',namespace1)
               if start is not None:
                   if (re.search('CCU',start.text)):
                       ccu_id.append(nbnid.text)
                       start.text=re.sub('CCU','NEC',(start.text))

               if end is not None:
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
        if(re.search('-CCU-',nbnid.text)):
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
        structurePointType=node1.find('nbn:structurePointType',namespace1)
        if structurePointType is not None:            
            if (structurePointType.text) == 'Pole' :
                nbntype=node1.find('nbn:type',nsmap)
                nbnid=node1.find('nbn:id',namespace1)
                if nbnid is not None:
                    hv_lv_nbn_id.append(nbnid.text)
                    if nbntype is not None :
                        nbntype.text='Joint Use'
                    else:
                        specification = ET.Element("nbn:type")
                        specification.text = "Joint Use"
                        node1.append(specification)

    ''' Script to convert plastic or pvc in duct type to plastic '''
    check_duct='.//gml:featureMember/nbn:duct'
    for node1 in root1.findall(check_duct, nsmap):
        ductType=node1.find('nbn:ductType',namespace1)
        if ductType is not None:
            if (ductType.text)=='Duct' :
                nbnmaterial=node1.find('nbn:material',nsmap)
                nbnid=node1.find('nbn:id',namespace1)
                if nbnid is not None:
                    hv_lv_1_nbn_id.append(nbnid.text)
                    if nbnmaterial is not None:
                        nbnmaterial.text='Plastic'
                    else:
                        specification = ET.Element("nbn:material")
                        specification.text = "Plastic"
                        node1.append(specification)

    check_duct='.//gml:featureMember/nbn:cable'
    for node1 in root1.findall(check_duct, nsmap):
        spec=node1.find('nbn:specification',namespace1)
        if spec is not None:
            if (spec.text)=='POWER_CABLE' :
                nbncableType=node1.find('nbn:cableType',nsmap)
                nbnid=node1.find('nbn:id',namespace1)
                if nbnid is not None:
                    hv_lv_2_nbn_id.append(nbnid.text)
                    if nbncableType is not None:
                        nbncableType.text='Electrical'
                    else:
                        specification = ET.Element("nbn:cableType")
                        specification.text = "Electrical"
                        node1.append(specification)

    check_duct='.//gml:featureMember/nbn:cable'
    for node1 in root1.findall(check_duct, nsmap):
        spec=node1.find('nbn:specification',namespace1)
        if spec is not None:
            if (spec.text)=='PWR_2X1C_PVC' :
                nbncableType=node1.find('nbn:cableType',nsmap)
                nbnid=node1.find('nbn:id',namespace1)
                if nbnid is not None:
                    hv_lv_2_nbn_id.append(nbnid.text)
                    if nbncableType is not None:
                        nbncableType.text='Electrical'
                    else:
                        specification = ET.Element("nbn:cableType")
                        specification.text = "Electrical"
                        node1.append(specification)

    check_duct='.//gml:featureMember/nbn:cable'
    for node1 in root1.findall(check_duct, nsmap):
        spec=node1.find('nbn:specification',namespace1)
        if spec is not None:
            if (spec.text)=='PWR_2X1C_PVC_E' :
                nbncableType=node1.find('nbn:cableType',nsmap)
                nbnid=node1.find('nbn:id',namespace1)
                if nbnid is not None:
                    hv_lv_2_nbn_id.append(nbnid.text)
                    if nbncableType is not None:
                        nbncableType.text='Electrical'
                    else:
                        specification = ET.Element("nbn:cableType")
                        specification.text = "Electrical"
                        node1.append(specification)
        
                    

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
    indent(root1)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    tree=ET.parse(updatedgml)
    
    root1 = tree.getroot()   
    

    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id', namespace1)
        nbnjointtype = node1.find('nbn:jointType', namespace1)
        if ((nbnjointtype.text) == 'CIU'):
            nbnspecific = node1.find('nbn:specification',namespace1)
            if nbnspecific is not None:
                if ((nbnspecific.text) == 'Unknown Unknown' or (nbnspecific.text) =='Channell 31D'):
                    nbnspecific.text = 'CU_OS_OJ_SMALL'
                    CIU.append(nbnid.text)
            
    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id',namespace1)               
        if (re.search('-FNO-',nbnid.text)):
            jointType=node1.find('nbn:jointType',namespace1)
            if jointType.text=='FTTB' :
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

                    
    for node1 in root1.findall('.//gml:featureMember/nbn:joint',nsmap):
        nbnid = node1.find('nbn:id',namespace1)
        if (re.search('-CSD-',nbnid.text)):
            jointType=node1.find('nbn:jointType',namespace1)             
            if jointType.text=="FTTB":
                jointType.text='Fibre'
                specification1=node1.find('nbn:specification',namespace1)
                if specification1 is not None:
                    if specification1.text == "NBN_FTTB":
                        specification1.text='D_TYCO_FIST-GCO2-BD-R12'
                        csdid.append(nbnid.text)


    indent(root1)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    tree=ET.parse(updatedgml)
    
    root1 = tree.getroot()         


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
                if ((specification.text) == 'FNO_48_CSD_MICRONODE'):
                    specification.text = 'ISAM_48'
                    csdfno.append(nbnid.text)

    
    
    
    indent(root1)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    
    tree=ET.parse(updatedgml)
    
    root = tree.getroot()  
    
    ''' Adding Structure route to cable'''  
 
    duct_dict = []    
    cable = []
    index = []
    for node1 in root.findall('.//gml:featureMember/nbn:cableDuct',nsmap):
        nbn_cable_id = node1.find('nbn:cableID',namespace1)
        nbn_duct_id = node1.find('nbn:ductID',namespace1)
        nbn_duct_index = node1.find('nbn:index',namespace1)
        if nbn_cable_id is not None and nbn_duct_id is not None and nbn_duct_index is not None:
            duct_dict.append(nbn_duct_id.text)
            cable.append(nbn_cable_id.text)
            index.append(nbn_duct_index.text)
    
    missed_structure_route = []
    duct_count = 0
    for cable, index in zip(cable,index):
        flag=1
        for node1 in root.findall('.//gml:featureMember/nbn:cableStructureRoute',nsmap):
            nbn_cable_id=node1.find('nbn:cableID',namespace1)
            nbn_cable_index=node1.find('nbn:index',namespace1)
            if(re.search(cable,nbn_cable_id.text) and index == nbn_cable_index.text):
                flag=0
                break;
        if(flag==1):
           missed_structure_route.append([duct_dict[duct_count],cable,index])
        duct_count += 1               
    print(missed_structure_route)                                                
    for key in missed_structure_route:
        for node1 in root.findall('.//gml:featureMember/nbn:ductStructureRoute',nsmap):
            nbn_duct_id = node1.find('nbn:ductId',namespace1)
            if nbn_duct_id is not None:
                if re.search(key[0],nbn_duct_id.text):
                    print("Yes added")
                    nbn_trench = node1.find('nbn:structureRouteId',namespace1)
                    Add_StructureRoute(key[1],nbn_trench.text,key[2])
                    break

    indent(root)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    tree = ET.parse(updatedgml)
    root1 = tree.getroot()

    for node1 in root1.findall('.//gml:featureMember/nbn:cableDuct',nsmap):
        cableID=node1.find('nbn:cableID',nsmap)
        nbncableID.append(cableID.text)        
            
    
    i=1
    l=0
    for node1 in root1.findall('.//gml:featureMember/nbn:cableDuct',nsmap):
        cableID=node1.find('nbn:cableID',nsmap)
        nbnid = node1.find('nbn:index',nsmap)        
        if nbnid is None:
            index1=ET.Element("nbn:index")
            index1.text=str(i)
            node1.append(index1)
            if l < len(nbncableID)-1 and nbncableID[l] != nbncableID[l+1]:
                i=1
            else:
                i=i+1
            l=l+1
            countofindex.append(cableID.text)
        if nbnid is not None:
            nbnid.text=str(i)
            if l < len(nbncableID)-1 and nbncableID[l] != nbncableID[l+1]:
                i=1
            else:
                i=i+1
            l=l+1

    for node1 in root1.findall('.//gml:featureMember/nbn:cableStructureRoute',nsmap):
        cableID=node1.find('nbn:cableID',nsmap)
        nbncableID1.append(cableID.text)        
            
    
    i=1
    l=0
    for node1 in root1.findall('.//gml:featureMember/nbn:cableStructureRoute',nsmap):
        cableID1=node1.find('nbn:cableID',nsmap)
        nbnid = node1.find('nbn:index',nsmap)        
        if nbnid is None:
            index2=ET.Element("nbn:index")
            index2.text=str(i)
            node1.append(index2)
            if l < len(nbncableID1)-1 and nbncableID1[l] != nbncableID1[l+1]:
                i=1
            else:
                i=i+1
            l=l+1
            countofindex1.append(cableID1.text)
        if nbnid is not None:
            nbnid.text=str(i)
            if l < len(nbncableID1)-1 and nbncableID1[l] != nbncableID1[l+1]:
                i=1
            else:
                i=i+1
            l=l+1


    indent(root1)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    tree=ET.parse(updatedgml)
    
    root1 = tree.getroot()
            
    for node1 in root1.findall('.//gml:featureMember/nbn:ductStructureRoute',nsmap):
        nbnid = node1.find('nbn:index',nsmap)               
        if nbnid is None:
            index=ET.Element("nbn:index")
            index.text="1"
            node1.append(index)

    for node1 in root1.findall('.//gml:featureMember/nbn:pcd', nsmap):        
        nbntech=node1.find('nbn:technology',nsmap)
        nbn=node1.find('nbn:id',nsmap)
        if nbntech is not None:
            if nbntech.text=="COPPER":
                nbnid = node1.find('nbn:specification', nsmap)
                if nbnid is None:
                    specification = ET.Element("nbn:specification")
                    specification.text = "VIRTUAL"
                    node1.append(specification)
                    pcdlist.append(nbn.text)
         
    indent(root1)
    tree.write(updatedgml,encoding='UTF-8',xml_declaration=True)
    writereport()
    print(updatedgml)
    print('GML generated Successfully')

except OSError as err:
    print("OS ERROR: {0}".format(err))
