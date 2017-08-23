#<input type = '<type>' name = '<name>' />

from flask import Flask, url_for, render_template
from app import app

import pymysql, time

#page/server-side interaction
@app.route('/')
def main():
    done = ' '
    target = int(time.strftime("%d")) # set the day to search throughout the database
    #accessing the database
    conn = pymysql.connect(host='localhost', port= 3306, user='root', passwd='hello', db='wowfactsheet')
    cur = conn.cursor()
    facts = cur.execute("SELECT wowday, wowinfo FROM wowfacts")

    for i in range(cur.rowcount):
        row = cur.fetchone()
        if row[0] == target:
            done = done +'\n' + row[1] #row[1] should contain the needed info
            print('\n',row[1])
    cur.close()
    conn.close()
    return render_template('finalizedstate.html', done = done)


#works if i do the interaction on the same page. i guess it felt a bit out of place for me.
#current problems: seperate the text/add the time/add set language for chinese wording
