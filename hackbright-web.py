from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github)
    return html

@app.route("/")    
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/make-student")
def make_student():
    return render_template("newstudent.html")


@app.route("/student-add", methods=['POST', 'GET'])
def student_add():
    """Add a student"""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    
    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("student_created.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github)

    return html


if __name__ == "__main__":
    app.run(debug=True)