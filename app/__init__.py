from flask import Flask
from flask_migrate import Migrate
from app.routes import main_bp
from app.database import init_db, db
from app.settings import Config

def create_app():
    app = Flask(
        __name__,
        template_folder = "templates"
                )
    
    app.config.from_object(Config)
    init_db(app)
    Migrate(app, db)
    app.register_blueprint(main_bp)
    with app.app_context():
        db.create_all()

    return app