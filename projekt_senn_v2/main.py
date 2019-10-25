
------------------------------------ODONI-----------------------------------------------------
"""Summary

Attributes:
    app (flask.app.Flask): Description
    app_main_path (TYPE): Description
    data_path (TYPE): Description
    data_storage_file (TYPE): Description
"""
import os
from pathlib import Path

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from libs import data
from libs import students

app = Flask("Dredd")

app_main_path = Path(os.path.abspath("/".join(os.path.realpath(__file__).split("/")[:-1])))
data_path = Path(os.path.abspath(app_main_path / ".." / "data"))
# app.secret_key = 'the random string'
data_storage_file = data_path / "students.json"


@app.route("/")
@app.route("/index")
def index():
    """Summary

    Returns:
        function: Description
    """
    return render_template("index.html")


@app.route("/students")
@app.route("/students/list")
def student_list():
    """Summary

    Returns:
        function: Description
    """
    students = data.load_json(data_storage_file)

    return render_template("students.html", students=students)


@app.route('/students/import', methods=['GET', 'POST'])
def import_students():
    """Summary

    Returns:
        function: Description
    """
    if request.method == 'POST':
        for file in request.files.getlist('file[]', None):
            if file.filename.split(".")[-1].lower() == "csv":
                csv_data = data.read_csv_stream(file)
                students.import_students_from_csv(csv_data, data_storage_file)

        return redirect(url_for('student_list'))

    return render_template("upload_teilnehmerliste.html")


@app.route("/student/")
@app.route("/student/<email>", methods=['GET', 'POST'])
def show_student(email=None):
    """Summary

    Args:
        email (None, optional): Description

    Returns:
        function: Description
    """

    # if no email
    if not email:
        return redirect(url_for('student_list'))

    # if student is being updated
    if request.method == 'POST':
        student = students.update_student(data_storage_file, email, request.form)
        return render_template("student.html", student=student)

    list_of_students = data.load_json(data_storage_file)

    # if student available
    if list_of_students.get(email):
        student = list_of_students[email]
        return render_template("student.html", student=student)
    else:
        return render_template("students.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)





------------------------------------ODONI-----------------------------------------------------