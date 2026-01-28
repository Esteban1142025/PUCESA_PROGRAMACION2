# =========================================================
# MÓDULO: GESTIÓN DE ACCESO Y SESIONES (main.py)
# =========================================================
# Este módulo controla el flujo principal de usuarios, incluyendo
# el inicio de sesión, el registro de nuevas unidades y el cierre de sesión.

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models import Usuario
from .. import db

# Definición del Blueprint para las rutas base y de autenticación
main_bp = Blueprint('main', __name__)

# ---------------------------------------------------------
# RUTA: PORTAL DE ENTRADA (HOME)
# ---------------------------------------------------------
@main_bp.route('/')
def home():
    """ Renderiza la interfaz de acceso (Login) del sistema """
    return render_template('login.html')

# ---------------------------------------------------------
# PROCESAMIENTO DE LOGIN
# ---------------------------------------------------------
@main_bp.route('/login_proceso', methods=['POST'])
def login_proceso():
    """ 
    Valida las credenciales del usuario contra los registros en MySQL.
    Si la validación es exitosa, se crea la sesión de usuario.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Consulta a la base de datos para buscar la identidad
    user = Usuario.query.filter_by(username=username).first()
    
    # Verificación de contraseña y carga de datos en la sesión (Session Flask)
    if user and user.password == password:
        session['user_id'] = user.id
        session['username'] = user.username
        session['rol'] = user.rol 
        return redirect(url_for('grafos.index'))
    
    # Manejo de error en caso de credenciales inválidas
    flash("ACCESO DENEGADO")
    return redirect(url_for('main.home'))

# ---------------------------------------------------------
# RUTA: REGISTRO DE NUEVAS UNIDADES
# ---------------------------------------------------------
@main_bp.route('/registro')
def registro():
    """ Muestra el formulario para dar de alta nuevos usuarios en el sistema """
    return render_template('registro.html')

# ---------------------------------------------------------
# PROCESAMIENTO DE REGISTRO (CRUD - Create)
# ---------------------------------------------------------
@main_bp.route('/registro_proceso', methods=['POST'])
def registro_proceso():
    """
    Gestiona la creación de nuevos usuarios realizando validaciones de 
    integridad, coincidencia de claves y disponibilidad de ID.
    """
    # Se obtienen los datos del HUD de registro
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # Validaciones de integridad: Verifica que no existan campos nulos
    if not username or not password or not confirm_password:
        flash("DATOS INCOMPLETOS: REVISE EL FORMULARIO")
        return redirect(url_for('main.registro'))

    # Validación de seguridad: Compara ambas contraseñas proporcionadas
    if password != confirm_password:
        flash("LAS CLAVES NO COINCIDEN")
        return redirect(url_for('main.registro'))

    # Verificación de existencia: Consulta si el nombre de usuario ya existe en la DB
    user_exists = Usuario.query.filter_by(username=username).first()
    if user_exists:
        flash("ID NO DISPONIBLE: ELIJA OTRO IDENTIFICADOR")
        return redirect(url_for('main.registro'))

    # Escritura en la base de datos MySQL mediante SQLAlchemy
    try:
        nuevo_usuario = Usuario(username=username, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("UNIDAD REGISTRADA: INICIE SESIÓN")
        return redirect(url_for('main.home'))
    except Exception as e:
        # En caso de error técnico, se revierte la transacción para mantener la integridad
        db.session.rollback()
        flash("FALLO DE SISTEMA: ERROR AL CREAR REGISTRO")
        return redirect(url_for('main.registro'))

# ---------------------------------------------------------
# CIERRE DE SESIÓN (LOGOUT)
# ---------------------------------------------------------
@main_bp.route('/logout')
def logout():
    """ 
    Limpia todos los datos almacenados en la sesión actual 
    y redirige al portal de acceso.
    """
    session.clear() 
    return redirect(url_for('main.home'))