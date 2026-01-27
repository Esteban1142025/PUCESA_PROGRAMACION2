from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registro de modulos (Blueprints)
    from .routes.main import main_bp
    from .routes.grafos import grafos_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(grafos_bp, url_prefix='/mapa')

    return app