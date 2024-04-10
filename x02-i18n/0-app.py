#!/usr/bin/env python3
"""flask module"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=True)
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)