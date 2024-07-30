#!/usr/bin/env python3
"""
Flask application to demonstrate translation using Babel
"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@app.route('/')
def home():
    """
    Home route that renders the home page with translated strings
    """
    return render_template(
                '3-index.html', title=_("home_title"), header=_("home_header")
                )


if __name__ == '__main__':
    app.run(debug=True)
