import os
list1=[]
list2=[]
source1 = r'S:\Technology\Design & Planning\000_Design at Scale Program\Design Enablement and Support Group\FDDD\3CBR\3CBR-21\04.QA\RD -DDD Package VX.X _DATE\3CBR-21_Splice_Joint_Records_1 new\3CBR-21_Splice_Joint_Records_1'
source2= r'S:\Technology\Design & Planning\000_Design at Scale Program\Design Enablement and Support Group\FDDD\3CBR\3CBR-21\04.QA\RD -DDD Package VX.X _DATE\3CBR-21_Splice_Joint_Records_1 new\3CBR-21_Splice_Joint_Records_1\updated'
for root, dirs, filenames in os.walk(source1):
    for f in filenames:
        #print f
        list1.append(f[:f.index('.')])
#print list1
for root, dirs, filenames in os.walk(source2):
    for f in filenames:
        #print f
        list2.append(f[:f.index('.')])
print [ i for i in list1 if i not in list2]
