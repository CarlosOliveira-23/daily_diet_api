from flask import Flask
from .database import init_app as init_db
from .main import main_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily_diet.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)
    app.register_blueprint(main_bp)

    return app
