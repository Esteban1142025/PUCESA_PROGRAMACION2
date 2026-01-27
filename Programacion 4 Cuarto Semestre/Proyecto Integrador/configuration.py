class Config:
    SECRET_KEY = 'tu_llave_secreta_aqui' 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/proyecto_mapa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False