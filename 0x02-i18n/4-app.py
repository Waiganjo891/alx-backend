#!/usr/bin/env python3
"""
Supported locales
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
SUPPORTED_LOCALES = ['en', 'fr']


def get_locale():
    """
    Determine the best match for supported languages.
    Check if 'locale' parameter is in the request and valid,
    return it if so. Otherwise, fall back to the default locale.
    """
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale
    return request.accept_languages.best_match(SUPPORTED_LOCALES)


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the index page.
    Display different content based on the locale.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
