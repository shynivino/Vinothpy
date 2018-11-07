import os

os.chdir(r"C:\Users\Reach User2\Desktop\KAPUT_BE")
os.system('dir > tmp.txt')
print (open('tmp.txt', 'r').read())
