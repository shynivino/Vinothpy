install 64bit oracle client
install 64bit python
pip install cx_oracle

import cx_Oracle
def NRM():
    ip = 'xx.xxx.xx.xx' #remedy
    port = 1522
    SID = 'xxxxxx' #service name
    username = 'YYYYY'
    password = 'YYYYY'

    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    db = cx_Oracle.connect(username, password, dsn_tns)
    cur = db.cursor()
    
 
    qry = """ select * from  table """
    
    cur.execute(qry)  
    print(list(cur))
    rec_data = cur.fetchall()
    db.close()
    
    results = []
   
    return True
NRM()
