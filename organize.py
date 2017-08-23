#!/usr/bin/env python

import pymysql, time

def info_creation(): 
    try:
        def telltime():
            print("Current Date: " + time.strftime("%m/%d/%Y"))
            print('------it runs through here-------')
            return("Current Date: " + time.strftime("%m/%d/%Y"))
        
        info = []
        telltime()
        #accesses the sql database
        target = int(time.strftime("%d"))
        conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd='hello', db='wowfactsheet')
        cur = conn.cursor()
        facts = cur.execute("SELECT wowday, wowinfo FROM wowfacts")
        def showinfo(info):
            print('----------so the program goes through the definitions-------')
            print(info)
            return(info)
        
        for i in range(cur.rowcount):
            row = cur.fetchone()
            if row[0] == target:
                info = row[1]
                showinfo(info) #should print(row[1]) to get info

        cur.close()
        conn.close()
    except IndexError:  
        return("its wrong?")

#prints None...but why? Is it because it is only reading the info_creation definiton?    


#current situation: need to reword/reformat code for Flask/website usage.
#need to also work on website design
#possible solution: define another variable and run it with the for loop to output each correct row
    
