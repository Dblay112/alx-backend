#!/usr/bin/env python3
"""
Babel module
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
    function that returns a user dictionary or None if
    the ID cannot be found or if login_as was not passed.
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return


@app.before_request
def before_request():
    """
    function and use the app.before_request decorator
    to make it be executed before all other functions
    before_request should use get_user to find a user if any,
    and set it as a global on flask.g.user.
    """
    g.user = get_user(request.args.get("login_as"))


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    hello world
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """method to determine the best
    match with our supported languages.
    """
    user_request = request.args.get('locale')
    if user_request:
        return user_request
    return request.accept_languages.best_match(["en", "fr"])


if __name__ == '__main__':
    app.run(debug=True)
