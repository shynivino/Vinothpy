with open(r"C:\Users\Reach User2\Desktop\national_vpn\export_ne_non_zero.csv") as csvfile:
    lines = csvfile.readlines()
dict_ne = []
ne_names = []
ne_name_counter = []
for line in lines:
    lin = line.split(",")
    dict_ne.append(lin[1])
from collections import Counter
dic = dict(Counter(dict_ne))
counter = 0
for k,v in sorted(dic.items(), key =lambda x:x[1] , reverse = True):
    ne_names.append(k)
    ne_name_counter.append(v)
    counter += 1
    if counter == 10:
        break
