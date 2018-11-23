import os,re

os.system(r'net user administrator > tmp.txt')
lines = open('tmp.txt', 'r').read()
os.remove('tmp.txt')
print(lines)
lines = lines.split('\n')
for line in lines:
    if re.search("Local Group Memberships.*\*Admin.*",line):
        print("ADMIN:",line);
    if re.search("Password last set.*",line):
        print("pwd:",line)
        
