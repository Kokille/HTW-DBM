import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask("Dredd")


@app.route("/")
@app.route("/index")
def index():
    """Summary

    Returns:
        function: Description
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)