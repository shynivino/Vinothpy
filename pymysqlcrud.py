# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 14:32:24 2018

@author: 1021240
"""
import pymysql

def connect():
    con = pymysql.connect('localhost','root','','tower_tool_database')
    cursor = con.cursor()
    return con,cursor


def insert(MaterialName,EMpa,GMpa):
    con,cursor = connect()
    #cursor.execute("insert into material values('S235',210000,80800,7850)")
    cursor.execute("insert into thicknessrange values('%s','%s',%f)"%(MaterialName,EMpa,GMpa))
    con.commit()
    con.close()
def update(MaterialName,EMpa,GMpa,Rho):
    con,cursor = connect()
    cursor.execute("update thicknessrange set e_mpa=%f,g_mpa='%s',where material_name = '%s'" % (EMpa,GMpa,MaterialName))
    con.commit()
    con.close()
    
def Delete(MaterialName):
    con,cursor = connect()
    cursor.execute("delete from thicknessrange where material_name = '%s'" %(MaterialName))
    con.commit()
    con.close()
def show():
    con,cursor = connect()
    cursor.execute("select * from thicknessrange")
    print (cursor.fetchall())
    con.close()

n=1 #this is the initial variable
while n != 5  :
        print "                1. Show \n \
               2. Insert \n \
               3. Update \n \
               4. Delete \n \
               5. Exit"
        n=int(raw_input("Enter Choice:"))
        
        if n == 1:
            print ("thicknessrange Database")
            show()
        elif n==2:
            MaterialName = raw_input("Enter Material Name")
            EMpa = raw_input("Enter the value of E_Mpa")
            GMpa = float(raw_input("Enter the value of G_Mpa"))
            insert(MaterialName,EMpa,GMpa)
        elif n==3:
            MaterialName = raw_input("Enter Material Name")
            EMpa = float(raw_input("Enter the value of E_Mpa"))
            GMpa = float(raw_input("Enter the value of G_Mpa"))
            Rho = float(raw_input("Enter the value of Rho"))
            update(MaterialName,EMpa,GMpa,Rho)
        elif n==4:
            MaterialName = raw_input("Enter Material Name")
            Delete(MaterialName)           
        elif n == 5 :
            pass
        else:
            print ("Invalid Option")
else :
        print("Exited")
