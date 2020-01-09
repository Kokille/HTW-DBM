import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

# Datastuff editing import
from libs.athletes import parse_athlete
from libs.team import (
    load_json,
    save_json,
)

app = Flask("Team")

# JSON files used as database.
DATEI_ATHLETE = 'athlete.json'
DATEI_COACH = 'coach.json'

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
        save_json(DATEI_COACH, request.form)
        return redirect("/team")
    return render_template("coaches.html")

"""------------------------------------------------------------------------------------------------------------"""

# Add Athletes
@app.route("/athletes", methods=["GET", "POST"])
def athletes():
    if request.method == "POST":
        save_json(DATEI_ATHLETE, request.form)
        return redirect("/team")
    return render_template("athletes.html")

"""------------------------------------------------------------------------------------------------------------"""

# Show Team
@app.route("/team")
def team():
    # Load JSON files
    all_coaches = load_json(DATEI_COACH)
    all_athletes = load_json(DATEI_ATHLETE)

    # Parse athletes by age / weight
    all_athletes = parse_athlete(all_athletes)

    return render_template("team.html", coaches=all_coaches, athletes=all_athletes)

"""------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)