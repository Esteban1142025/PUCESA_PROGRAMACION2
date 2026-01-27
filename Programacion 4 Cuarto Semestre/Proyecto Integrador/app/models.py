from . import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), default='usuario') # 'usuario', 'ingeniero', 'admin'

    def get_nivel(self):
        """Retorna el nivel numérico de acceso"""
        niveles = {
            'admin': 3,
            'ingeniero': 2,
            'usuario': 1
        }
        # Si el rol no está en el dict, por defecto es nivel 1
        return niveles.get(self.rol, 1)

class RutaFavorita(db.Model):
    __tablename__ = 'rutas_favoritas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    nombre_ruta = db.Column(db.String(100))
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))
    bloqueos = db.Column(db.Text)
    
class EstadoMapa(db.Model):
    __tablename__ = 'estado_mapa'
    id = db.Column(db.Integer, primary_key=True)
    # Guardaremos los nodos bloqueados como una cadena separada por comas (ej: "1,2,5,Nucleo")
    nodos_restringidos = db.Column(db.Text, default="")