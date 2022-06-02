# import "packages" from flask
import json

# import app as app
from flask import render_template, redirect, request, url_for, send_from_directory
from flask_login import login_required

from __init__ import app, login_manager
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from cruddy.login import login, logout, authorize
# from uploady.app_upload import app_upload
from notey.app_notes import app_notes
from events.app_events import app_events

# app.register_blueprint(app_upload)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)
app.register_blueprint(app_events)


# create a Flask instance
# connects default URL to render index.html

@app.route('/logout/', methods=["GET", "POST"])
@login_required
def main_logout():
    logout()
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    app.config['NEXT_PAGE'] = request.endpoint
    return redirect(url_for('main_login'))


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def main_login():
    # obtains form inputs and fulfills login requirements
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):
            if (email == "test@test.com") and (password == "test123"): # this can be replaced with whatever login is needed
                return redirect(url_for('crud.crud'))
            else:
                return redirect(url_for('crud.crud_view'))
    # if not logged in, show the login page
    return render_template("login.html")


@app.route('/authorize/', methods=["GET", "POST"])
def main_authorize():
    error_msg = ""
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")  # password should be verified
        if password1 == password2:
            if authorize(user_name, email, password1):
                return redirect(url_for('main_login'))
        else:
            error_msg = "Passwords do not match"
    # show the auth user page if the above fails for some reason
    return render_template("authorize.html", error_msg=error_msg)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about/')
def about():
    return render_template("about.html")



@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


@app.route('/activity')
def activity():
    return render_template("activity.html")

@app.route('/generator')
def generator():
    return render_template("generator.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    ),
