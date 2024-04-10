#!/usr/bin/env python3
"""flask module"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    hello world
    """
    return render_template('index.html')
