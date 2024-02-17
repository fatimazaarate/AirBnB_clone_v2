#!/usr/bin/python3
""" a script that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display_states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
