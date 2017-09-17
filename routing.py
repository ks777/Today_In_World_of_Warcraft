#<input type = '<type>' name = '<name>' />

from flask import Flask, url_for, render_template
from app import app

import pymysql, time

#page/server-side interaction
@app.route('/')
def main():
    done = [ ]
    target = int(time.strftime("%d")) # set the day to search throughout the database
    #accessing the database
    conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd='hello', db='wowfactsheet', charset = 'utf8')
    cur = conn.cursor()
    facts = cur.execute("SELECT wowday, wowinfo FROM wowfacts")

    for i in range(cur.rowcount):
        row = cur.fetchone()
        if row[0] == target:
            done.append(row[1]) #row[1] should contain the needed info
            print("""%s\n""" %(row[1]))
    #print(len(done))
    cur.close()
    conn.close()
    if target == 7:
        return render_template('finalizedstate2.html', done = done)
# Right now, i`m leaving these commented. While I can check If this method will work,
# I have decided to finish this since i have a bit of time.
    elif target == 13:
        return render_template('finalizedstate3.html', done = done)
    elif target == 16:
        return render_template('finalizedstate4.html', done = done)
    elif target == 23:
        return render_template('finalizedstate5.html', done = done)
    elif target == 25:
        return render_template('finalizedstate6.html', done = done)
    elif target == 30:
        return render_template('finalizedstate7.html', done = done)
    else:
        return render_template('finalizedstate.html', done = done)

#Only problem/task left before 100% completion: There are 2 dates (13th) that need to have 2 different backgrounds
#Aside from javascript, i will need to figure out a way to implement this.
#Like i said, something i`ll improve over time/not really focused on this project right now.
