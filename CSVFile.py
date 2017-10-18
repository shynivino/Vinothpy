import csv
cupid_match=['CHECK','UserName','Shipment Id']
with open('C:\NPAM\Book2.csv', 'wb') as csvFile:  # creating the consolidation file
    fieldnames = cupid_match
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    print("Header Writen while creating")
    #for i in range(0,len(cupid_match)):
       
    writer.writerow({'UserName':cupid_match})
csvFile.close()
