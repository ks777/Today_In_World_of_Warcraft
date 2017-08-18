from flask import Flask, url_for, render_template
from app import app
import organize


#page/server-side interaction
@app.route('/')
def commence():
    print("it gets here")
    done = organize.info_creation()
    return render_template('finalizedstate.html', done = done)

