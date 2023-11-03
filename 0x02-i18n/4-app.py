#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = babel.default_locale
    BABEL_DEFAULT_TIMEZONE = babel.default_timezone.zone


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale"""
    lang = request.args.get("locale")
    if lang and lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """ index route"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
