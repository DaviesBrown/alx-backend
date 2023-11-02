#!/usr/bin/env python3
"""
flask app
"""
from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz


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
    BABEL_DEFAULT_TIMEZONE = babel.default_timezone


flask_app.config.from_object(Config)


def get_user() -> Union[Dict, None]:
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


@flask_app.context_processor
def inject_user():
    """inject user"""
    if g.user is not None:
        return dict(g.user)
    else:
        return {}


@babel.localeselector
def get_locale() -> str:
    """ get locale"""
    lang = request.args.get("locale")
    if lang and lang in flask_app.config["LANGUAGES"]:
        return lang
    if g.user and g.user["locale"] in flask_app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(flask_app.config['LANGUAGES'])


babel.t
def get_timezone():
    """get timezone"""
    print(request.args)
    tz = request.args.get("timezone")
    if tz:
        try:
            tz = pytz.timezone(tz)
            print(tz.zone)
            return tz.zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 
    """ user = getattr(g, 'user', None)
    print(user)
    if user is not None:
        try:
            user = pytz.timezone(user)
            return user.timezone
        except pytz.exceptions.UnknownTimeZoneError:
            return """


@flask_app.route("/", strict_slashes=False)
def index():
    """ index route"""
    return render_template("7-index.html")


if __name__ == "__main__":
    flask_app.run(debug=True)
