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


@app.route('/states_list', strict_slashes=False)
def display_states_list_html():
    """ Method that displays an HTML page that lists states """
    state_dict = storage.all(classes["State"])
    return render_template('7-states_list.html', state=state_dict)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_state_html():
    """ Method that displays an HTML page that lists states
        and cities in that state
    """
    state_dict = storage.all(classes["State"])
    # Key is State obj, value is a list of city obj in that state
    state_and_city_dict = {}
    for key, value in state_dict.items():
        state_and_city_dict[value] = value.cities
    return render_template('8-cities_by_states.html', cs=state_and_city_dict)


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


@app.route('/hbnb_filters', strict_slashes=False)
def display_web_static_html():
    """ Method displays the HTML page for web static """
    return render_template('10-hbnb_filters.html')


@app.teardown_appcontext
def close_session(exception):
    """ Method that closes the session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
