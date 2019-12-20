import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

#Datastuff editing import
from libs import athletes
from libs import coaches as coaches_lib
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
        coaches_lib.save(form.request)
        return redirect("/team")
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
            "name": "Senn",
            "vorname": "Kilian",
            "jahrgang": "1998"
        },
         {
            "name": "Sprenger",
            "vorname": "Aileen",
            "jahrgang": "1995"
        }
    ]
    dict_athlete = [
        {
            "name": "Senn",
            "vorname": "Kilian",
            "disziplin": "Kumite Male",
            "kategorie": "U16, +58kg"
        }
    ]
    return render_template("team.html", coaches=dict_coach, athletes=dict_athlete )

"""------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)