# import "packages" from flask
import json

# import app as app
from flask import render_template, request
from __init__ import app

# create a Flask instance

# connects default URL to render index.html


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run( debug=True)