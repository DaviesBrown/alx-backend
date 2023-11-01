#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template
from flask_babel import Babel

flask_app = Flask(__name__)
babel = Babel(flask_app)


class Config(object):
    """ config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "es"
    BABEL_DEFAULT_TIMEZONE = babel.default_timezone.zone


flask_app.config.from_object(Config)
# print(flask_app.config)


@flask_app.route("/", strict_slashes=False)
def index():
    """ index route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    flask_app.run()
