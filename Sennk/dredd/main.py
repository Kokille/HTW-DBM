import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    """Summary

    Returns:
        function: Description
    """
    return render_template("index.html")

"""------------------------------------------------------------------------------------------------------------"""

@app.route("/coaches")
def coaches():
    """Summary

    Returns:
        function: Description
    """
    return render_template("coaches.html")

"""------------------------------------------------------------------------------------------------------------"""

@app.route("/athletes")
def athletes():
    """Summary

    Returns:
        function: Description
    """
    return render_template("athletes.html")

"""------------------------------------------------------------------------------------------------------------"""

@app.route("/team")
def team():
    """Summary

    Returns:
        function: Description
    """
    return render_template("team.html")

"""------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)