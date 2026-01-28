from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration import Config

# Inicialización de la extensión SQLAlchemy fuera de la fábrica
# Esto permite importar 'db' en otros archivos sin causar importaciones circulares
db = SQLAlchemy()

def create_app():
    """
    Fábrica de la aplicación: Configura e inicializa la instancia de Flask.
    """
    app = Flask(__name__)
    
    # Carga la configuración (Secret Key, URI de Base de Datos, etc.) desde Config
    app.config.from_object(Config)

    # Vincula la instancia de la base de datos con la aplicación Flask actual
    db.init_app(app)

    # Registro de modulos (Blueprints)
    # Los Blueprints permiten organizar las rutas en archivos separados para mayor escalabilidad
    from .routes.main import main_bp
    from .routes.grafos import grafos_bp
    
    # Registro del Blueprint principal (Home, Login, Registro)
    app.register_blueprint(main_bp)
    
    # Registro del Blueprint de Grafos con un prefijo de URL específico
    # Todas las rutas dentro de grafos_bp comenzarán con /mapa (ej: /mapa/calcular)
    app.register_blueprint(grafos_bp, url_prefix='/mapa')

    return app