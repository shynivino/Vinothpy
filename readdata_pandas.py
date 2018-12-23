import pandas as pd
from sqlalchemy import create_engine

 data = pd.read_csv(r'C:\Users\Reach User2\Documents\export2.txt', sep=";@", header=None,engine='python')
 data.columns = ["ne_name", "ne_ip", "service_type", "service_id","sap","description","customer_name","date","time","raw_egress","raw_ingress","ex_tx","in_rx","duration"]
 data = data.fillna(0)

 greater_tx = data["ex_tx"] > 0
 greater_rx = data["in_rx"] > 0
 non_zero = (data[greater_rx & greater_tx])
 non_zero_links = [];
 for i in range(len(non_zero['ne_name'])):
     non_zero_links.append(non_zero['ne_name'][i] + non_zero['ne_ip'][i] + non_zero['service_type'][i] + str(non_zero['service_id'][i]) + non_zero['sap'][i])
 with open("non_zero_ne.txt","w") as out:
     for j in non_zero_links:
         out.writelines(j+'\n')


 print(list(data.columns.values))
 data = data[:5]
 engine = create_engine("mysql://root:@localhost/ipvpn")

 data.to_sql(name='ipvpn_ne_export_db1',con=engine,if_exists='append')

 with open(r'C:\Users\Reach User2\Documents\export2.txt') as out:
     lines=out.readlines()
 with open(r'C:\Users\Reach User2\Desktop\ne_unique.txt') as zero:
     zeroline = zero.readlines()
 collectzero = [];
 for zero in zeroline:
     flag = 0
     for line in lines:
         ne = line.strip().split(";@")
         tmp = ne[0]+ne[1]+ne[2]+ne[3]+ne[4]
         in_rx = ne[-3]
         ex_tx = ne[-2]

         in_rx = '0.0000' if in_rx == '' else in_rx
         ex_tx = '0.0000' if ex_tx == '' else ex_tx

         if zero.strip() == tmp and (float(in_rx) != 0.0000 or float(ex_tx) != 0.0000):
             flag = 1
             break
     if flag == 0:
         print(zero)
         collectzero.append(zero)

 with open("zerotraffic.txt","a") as out:
     for zero in collectzero:
         out.writelines(zero+'\n')

df = pd.read_csv(r'C:\Users\Reach User2\Documents\export2.txt', sep=";@", header=None,engine='python')
df.columns = ["ne_name", "ne_ip", "service_type", "service_id","sap","description","customer_name","date","time","raw_egress","raw_ingress","ex_tx","in_rx","duration"]

df[["in_rx", "ex_tx"]] = df[["in_rx", "ex_tx"]].apply(pd.to_numeric)
de = df.loc[(df['in_rx']) == 0 & (df['ex_tx']) == 0]
print(de)

