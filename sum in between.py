#sum up list of values between 3 and 8(inclusive both) and assume 8 occured after 3.
#input: a=[1,2,5,3,7,9,4,5,8,6,5,2,5]
#output:36

a=[1,2,5,3,7,9,4,5,8,6,5,2,5]
sum=0

for i in range(len(a)):
  if a[i]==3:
    break
for j in range(i,len(a)):
  sum+=a[j]
  if a[j]==8:
    break
print("sum:",sum)

