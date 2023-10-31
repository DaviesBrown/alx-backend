#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template

flask_app = Flask(__name__)

@flask_app.route("/", ["GET"], strict_slashes=False)
def index():
    return render_template("0-index.html")

if __name__ == "__main__":
    flask_app.run()