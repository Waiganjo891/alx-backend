#!/usr/bin/env python3
"""
This module sets up a Flask application with Babel for
internationalization and localization. It includes a
locale selector to determine the best match for the
user's preferred languages.
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
SUPPORTED_LANGUAGES = ['en', 'es', 'fr']


@app.route('/')
def index():
    """Render the index page."""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    Select the best match for the user's preferred languages
    from the supported languages. The function uses
    request.accept_languages to get the list of languages accepted
    by the client and matches it against the supported languages.
    Returns:
        str: The best matched language code or 'en' if no match is found.
    """
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


if __name__ == '__main__':
    app.run(debug=True)
