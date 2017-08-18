#!/usr/bin/env python

import pymysql, time

def info_creation():
    return("Current Date: " + time.strftime("%m/%d/%Y"))
    target = int(time.strftime("%d"))
    conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd=' ', db='wowfactsheet')
    cur = conn.cursor()
    facts = cur.execute("SELECT wowday, wowinfo FROM wowfacts")

    for i in range(cur.rowcount):
        row = cur.fetchone()
        if row[0] == target:
            return("\n%s" %(row[1]))

    cur.close()
    conn.close()
