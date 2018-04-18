#!/usr/bin/python3
""" Module that starts a Flask web application with routes and web templates.
    - Uses FileStorage and DBStorage classes.
    - One route is /states_list and calls a function that displays HTML page.
"""

from flask import Flask
from flask import render_template
import models


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states_list_html():
    """ Method that displays an HTML page that lists states """
    state_dict = storage.all(models.classes["State"])
    return render_template('7-states_list.html', state_dict)


@app.teardown_appcontext()
def close_session():
    """ Method that closes the session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
