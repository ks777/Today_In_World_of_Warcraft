#!/usr/bin/env python

import pymysql, time
print("Current Date: " + time.strftime("%m/%d/%Y"))
target = int(time.strftime("%d"))
print(target)

conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd=' ', db='wowfactsheet')

print("connection established")
cur = conn.cursor()
facts = cur.execute("SELECT wowday, wowinfo FROM wowfacts")

print("attempting to print out a row to confirm possibility")
for i in range(cur.rowcount):
    row = cur.fetchone()
    if row[0] == target:
        print("\n%s" %(row[1]))
#    elif row[0] != target:
 #       print(row)
  #      print("so at least this works")

#prints all the information...yet i need to print certain rows.
print("process achieved! congrates")

#testing out pymysql and python integration. seems quite fluid
#using local database...need to figure out how to take database for github purposes

cur.close()
conn.close()
