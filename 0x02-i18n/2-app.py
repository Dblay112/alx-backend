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
    return request.accept_languages.best_match(["en", "fr"])


if __name__ == '__main__':
    app.run(debug=True)
