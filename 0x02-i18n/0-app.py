#!/usr/bin/env python3
"""
This is the main module for the basic
Flask app. It sets up a simple web server
with a single route.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html template with
    a welcome message.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
