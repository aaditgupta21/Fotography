import markdown
from flask import Blueprint, render_template
from flask_login import login_required
from cruddy.model import Events

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_events = Blueprint('events', __name__,
                      url_prefix='/events',
                      template_folder='templates/events/',
                      static_folder='static',
                      static_url_path='static')


def events_all():
    return events_all_alc()


# SQLAlchemy extract all users from database
def events_all_alc():
    table = Events.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready



@app_events.route('/')
@login_required
def events():
    return render_template("events.html")

# Notes create/add
