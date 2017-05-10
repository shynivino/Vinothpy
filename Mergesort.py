#merge 2 sorted list and merged one also in sorted 
a=[1,4,7,9]
b=[3,5,8,10,34]
aindex=0
bindex=0
c=[]
while aindex < len(a) and bindex < len(b):
    if a[aindex] < b[bindex]:
        c.append(a[aindex])
        aindex+=1
    else:
        c.append(b[bindex])
        bindex+=1
if aindex==len(a):
    c.extend(b[bindex:])
else:
    c.append(a[aindex:])
print ("sorted list:",c)
