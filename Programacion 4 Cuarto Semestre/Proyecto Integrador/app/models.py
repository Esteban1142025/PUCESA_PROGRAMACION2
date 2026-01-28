from . import db

# Definición del modelo de Usuario para autenticación y permisos
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # El rol determina qué acciones puede realizar en el mapa de Mindustry
    rol = db.Column(db.String(20), default='usuario') # 'usuario', 'ingeniero', 'admin'

    def get_nivel(self):
        """Retorna el nivel numérico de acceso"""
        # Sistema de jerarquía para validación de rutas protegidas
        niveles = {
            'admin': 3,
            'ingeniero': 2,
            'usuario': 1
        }
        # Si el rol no está en el dict, por defecto es nivel 1 (seguridad básica)
        return niveles.get(self.rol, 1)

# Modelo para persistencia de rutas personalizadas por el usuario
class RutaFavorita(db.Model):
    __tablename__ = 'rutas_favoritas'
    id = db.Column(db.Integer, primary_key=True)
    # Relación de llave foránea con la tabla usuarios
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    nombre_ruta = db.Column(db.String(100))
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))
    # Almacena los nodos evitados durante el cálculo de la ruta
    bloqueos = db.Column(db.Text)
    
# Modelo para el control administrativo del mapa global
class EstadoMapa(db.Model):
    __tablename__ = 'estado_mapa'
    id = db.Column(db.Integer, primary_key=True)
    # Guardaremos los nodos bloqueados como una cadena separada por comas (ej: "1,2,5,Nucleo")
    # Estos nodos afectan a todos los usuarios que intenten trazar rutas
    nodos_restringidos = db.Column(db.Text, default="")