#!/usr/bin/python3
""" Module that starts a Flask web application with routes and web templates.
    - Uses FileStorage and DBStorage classes.
    - One route is /states and calls a function that displays
    States in an HTML page.
    - One route is /states/<id> and calls a function that will display
    a specific State in the HTML page.
"""

from flask import Flask
from flask import render_template
from models import storage, classes

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states_html():
    """ Method that displays an HTML page that lists states
        in an HTML page
    """
    state_dict = storage.all(classes["State"])
    return render_template('9-states.html', single=None, state=state_dict)


@app.route('/states/<id>', strict_slashes=False)
def display_state_id(id):
    """ Method that displays an HTML page that lists the
        State specified by the id
        - If the id is wrong, will display a default HTML page
    """
    state_dict = storage.all(classes["State"])
    # Key is State Object, Value is list of cities in that state
    state_and_city_dict = {}
    state_key = "State.{}".format(id)
    if state_key in state_dict:
        state_obj = state_dict[state_key]
        state_and_city_dict[state_obj] = state_obj.cities
        return render_template('9-states.html',
                               single=state_and_city_dict, state=None)
    else:
        return render_template('9-states.html', single=None, state=None)


@app.teardown_appcontext
def close_session(exception):
    """ Method that closes the session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
