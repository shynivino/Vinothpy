from xml.etree.ElementTree import parse,Element
import xml.etree.ElementTree as ET
import re,os,csv

tree=ET.parse('./test.xml')
root=tree.getroot()
print (root)
for node1 in root.findall('cat[book]'):
    for aut in node1.findall('book'):
        aut1=aut.find('author')
        print(aut1.text)
        if aut1.text=="O'Brien, Tim":
           node1.remove(aut)
           print("Deleted")
tree.write('./test1.xml',encoding='UTF-8',xml_declaration=True)
