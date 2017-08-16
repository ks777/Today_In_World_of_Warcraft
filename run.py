#!/usr/bin/env python

import pymysql, time
print("Current Date: " + time.strftime("%m/%d/%Y"))

conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd=' ', db='wowfactsheet')

print("connection established")
cur = conn.cursor()
facts = cur.execute("SELECT wowinfo FROM wowfacts")
data = cur.fetchall()

#prints all the information...yet i need to print certain rows.
print("attempting to print out a row to confirm possibility")
print(facts)
#for row in data:
#   print(row[0], row[1])
print("process achieved! congrates")

#testing out pymysql and python integration. seems quite fluid
#using local database...need to figure out how to take database for github purposes

cur.close()
conn.close()
