import sqlite3
conn = sqlite3.connect('C:/Users/Reach User2/Documents/PeeringManager/peering-manager-report_integration/db.sqlite3')     
cur = conn.cursor()
cur.execute("SELECT * FROM tasks")

rows = cur.fetchall()

for row in rows:
    print(row)
 
