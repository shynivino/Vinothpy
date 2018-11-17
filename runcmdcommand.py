import os
os.system(r'tasklist/svc > tmp.txt')
lines = open('tmp.txt', 'r').read()
os.remove('tmp.txt')
print(lines)
