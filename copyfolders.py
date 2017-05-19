import shutil
import csv,os
samlist=[]
completedsam=[]
def readcsv():
    with open('sam3.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            samlist.append(row[0])
    print("SAMS",len(samlist))      
    subdirectories = os.listdir("S:/Technology/Design & Planning/000_Design at Scale Program/Design Enablement and Support Group/Pole Data Cleansing/New SAMs Stream B and C/4. Re-Work")
    print("Folders",len(subdirectories))
    print("###################################### Present List #######################################")
    for sam in samlist:
        if sam in subdirectories:
            print(sam)
            completedsam.append(sam)
            
def writecsv():
    with open('sam4.csv', 'wb') as f:
        writer1 = csv.writer(f,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer1.writerow("########Completed#############")
        for sam in completedsam:
            writer1.writerow(sam)
        
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

if __name__== "__main__":

    readcsv()
    writecsv()
    for sam in completedsam:
        copyDirectory("S:/Technology/Design & Planning/000_Design at Scale Program/Design Enablement and Support Group/Pole Data Cleansing/New SAMs Stream B and C/1.In progress"+"/"+sam,"S:/Technology/Design & Planning/000_Design at Scale Program/Design Enablement and Support Group/Pole Data Cleansing/New SAMs Stream B and C/Backup"+"/"+sam)
