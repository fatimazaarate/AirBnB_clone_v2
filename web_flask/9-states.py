#!/usr/bin/python3
""" a script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def display_states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """display a HTML page: (inside the tag BODY)"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state, id=id)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
