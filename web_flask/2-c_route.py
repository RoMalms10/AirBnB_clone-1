#!/usr/bin/python3
""" This module will import flask for a web application.
    Web application needs to be waiting on 0.0.0.0 and port 5000.
    One route is / and will call a function that displays "Hello HBNB!"
    One route is /hbnb and will call a function that displays "HBNB"
    One route is /c/<text> and will call a function that prints "C" followed
    by the text that is put into the route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def print_hello_HBNB():
    """ Prints a message when the route / is taken in the web application """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """ Prints a different mesage when the route is /hbnb """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def print_c_plus_text():
    """ Prints C and then the text that is added to the route """
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
