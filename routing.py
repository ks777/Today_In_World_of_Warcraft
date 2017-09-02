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
# I don`t want to lose sleep over it. So atm, i`ll check back in the 7th of the month, and if i works, i`ll proceed.
# Otherwise the month is up and i should move on to other projects.
#    elif target == 13:
#    elif target == 15:
#    elif target == 23:
#    elif target == 25:
#    elif target == 30:
    else:
        return render_template('finalizedstate.html', done = done)

#works if i do the interaction on the same page. i guess it felt a bit out of place for me.
#current problems: seperate the text/add the time/add set language for chinese wording
