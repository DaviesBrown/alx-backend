#!/usr/bin/env python3
"""
flask app
"""
from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

flask_app = Flask(__name__)
babel = Babel(flask_app)


class Config(object):
    """ config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = babel.default_locale
    BABEL_DEFAULT_TIMEZONE = babel.default_timezone.zone


flask_app.config.from_object(Config)


def get_user() -> Union[Dict, None]:
    """get user"""
    user_id = request.args.get("login_as")
    try:
        user_id = int(user_id)
    except Exception:
        return None
    if user_id in users:
        return users[user_id]
    return None


@flask_app.before_request
def before_request():
    """before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ get locale"""
    lang = request.args.get("locale")
    if lang and lang in flask_app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(flask_app.config['LANGUAGES'])


@flask_app.route("/", strict_slashes=False)
def index():
    """ index route"""
    return render_template("5-index.html", user=g.user)


if __name__ == "__main__":
    flask_app.run()
