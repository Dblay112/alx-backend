#!/usr/bin/env python3
"""Basic Babel setup"""
from Flask import flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config():
    """base class for configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
