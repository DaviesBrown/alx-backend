#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel


flask_app = Flask(__name__)
babel = Babel(flask_app)


class Config(object):
    """ config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = babel.default_timezone.zone


flask_app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ get locale
        returns best match for locale
    """
    return request.accept_languages.best_match(flask_app.config['LANGUAGES'])


@flask_app.route("/", strict_slashes=False)
def index() -> str:
    """ index route"""
    return render_template("2-index.html")


if __name__ == "__main__":
    flask_app.run()
