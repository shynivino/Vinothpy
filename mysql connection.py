''' python 3.5 V:
download mysql API for python
go to mysql dir:
python setup.py build
python setup.py install or pip install pymysql'''
## import pymysql
start XAMPP start Mysql
import pymysql

c=MySQLdb.connect('localhost','root','')
c=pymysql.connect('localhost','root','')
cursor=c.cursor()
query="CREATE DATABASE TESTDB"
cursor.execute(query)
c=pymysql.connect('localhost','root','','TESTDB')
cursor=c.cursor()
q="Create table emp(id integer, name varchar(20),age integer)"
cursor.execute(q)
q="insert into emp values(1,'huli',28)"
cursor.execute(q)
q="select *from emp"
cursor.execute(q)
print(q)
r=cursor.fetchall()
q="insert into emp values(1,'kavya',24)"
cursor.execute(q)
q="select *from emp"
cursor.execute(q)
r=cursor.fetchall()
print(r)
c.close()

