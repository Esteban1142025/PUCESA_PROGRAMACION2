class Config:
    # Llave para cifrar las sesiones de usuario y proteger contra ataques CSRF
    SECRET_KEY = 'Mindustry' 
    
    # URI de conexión: 
    # Protocolo: mysql+pymysql (usa el driver PyMySQL)
    # Usuario: root | Contraseña: [vacía] | Host: localhost | DB: proyecto_mapa
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/proyecto_mapa'
    
    # Desactiva el sistema de notificaciones de cambios de SQLAlchemy para ahorrar recursos 
    # y evitar advertencias en la consola (overhead innecesario)
    SQLALCHEMY_TRACK_MODIFICATIONS = False