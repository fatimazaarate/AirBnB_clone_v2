#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """
    Display “n is a number” only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Display “n is a HTML page only if n is an integer.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
