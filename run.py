#!/usr/bin/env python

import pymysql

conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd=' ', db='wowfactsheet')

print("connection established")
cur = conn.cursor()
facts = cur.execute("SELECT * FROM wowfactsheet.wowfacts")

print("attempting to print out a row to confirm possibility")
print(facts)
for row in cur:
    print(row)
print("process achieved! congrates")

#testing out pymysql and python integration. seems quite fluid
#using local database...need to figure out how to take database for github purposes

cur.close()
conn.close()
