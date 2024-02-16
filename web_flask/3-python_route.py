#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    Display Hello HBNB.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    Display HBNB.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """
    Display “C ” followed by the value of the text variable.
    Args:
        text (str): The text provided in the URL parameter.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    """
    Display “Python ”, followed by the value of the text variable.
    Args:
        text (str): The text provided in the URL parameter.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
