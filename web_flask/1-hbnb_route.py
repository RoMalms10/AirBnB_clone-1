#!/usr/bin/python3
""" This module will import flask for a web application.
    Web application needs to be waiting on 0.0.0.0 and port 5000.
    One route is / and will call a function that displays "Hello HBNB!"
    One route is /hbnb and will call a function that displays "HBNB"
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Prints a message when the route / is taken in the web application """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a different mesage when the route is /hbnb """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
