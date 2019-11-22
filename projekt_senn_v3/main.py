




@app.route("/")
@app.route("/index")
def index():
    """Summary

    Returns:
        function: Description
    """
    return render_template("index.html")


    