import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

#Datastuff editing import
from libs import athletes
from libs import coaches
from libs import team

app = Flask("Team")

"""------------------------------------------------------------------------------------------------------------"""

#Landingpage
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

"""------------------------------------------------------------------------------------------------------------"""

#Add Coaches
@app.route("/coaches", methods=["GET", "POST"])
def coaches():
    if request.method == "POST":
        coaches.safe_entry_form(request.form)
        """name = request.form["name"]
        return render_template("team.html", name=name, vorname=vorname, jahrgang=jahrgang)"""
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
    dict_coach = [
        {
            "name": "Franz",
            "vorname": "Franz",
            "jahrgang": "900"
        },
         {
            "name": "Franz",
            "vorname": "Franz",
            "jahrgang": "900"
        },
         {
            "name": "Franz",
            "vorname": "Franz",
            "jahrgang": "900"
        }
    ]
    return render_template("team.html", coaches=dict_coach )

"""------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)