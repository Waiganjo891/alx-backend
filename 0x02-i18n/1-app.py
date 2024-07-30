#!/usr/bin/env python3
"""
This module sets up a Flask application with
Babel integration for language translations.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for the Flask application.
    Attributes:
        LANGUAGES (list): Supported
        languages for the application.
        BABEL_DEFAULT_LOCALE
        (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE
        (str): Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index():
    """
    Route handler for the home page.
    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
