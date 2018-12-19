from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
db = SQLAlchemy()


def current_app():
    app.config.from_object(Config)
    db.init_app(app)
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)
    # app.register_blueprint(login_blu)
    return app