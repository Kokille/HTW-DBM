import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)


#Landingpage
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

"""------------------------------------------------------------------------------------------------------------"""

#Add Coaches
@app.route("/coaches")
def coaches():
    return render_template("coaches.html")

"""------------------------------------------------------------------------------------------------------------"""

#Add Athletes
@app.route("/athletes")
def athletes():
    return render_template("athletes.html")

"""------------------------------------------------------------------------------------------------------------"""

#Show Team
@app.route("/team")
def team():
    return render_template("team.html")

"""------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)