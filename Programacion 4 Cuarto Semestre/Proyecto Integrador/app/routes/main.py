from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models import Usuario
from .. import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('login.html')

@main_bp.route('/login_proceso', methods=['POST'])
def login_proceso():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = Usuario.query.filter_by(username=username).first()
    
    if user and user.password == password:
        session['user_id'] = user.id
        session['username'] = user.username
        session['rol'] = user.rol 
        return redirect(url_for('grafos.index'))
    
    flash("ACCESO DENEGADO")
    return redirect(url_for('main.home'))

@main_bp.route('/registro')
def registro():
    return render_template('registro.html')

@main_bp.route('/registro_proceso', methods=['POST'])
def registro_proceso():
    # Se obtienen los datos del HUD de registro
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    #Validaciones de integridad
    if not username or not password or not confirm_password:
        flash("DATOS INCOMPLETOS: REVISE EL FORMULARIO")
        return redirect(url_for('main.registro'))

    if password != confirm_password:
        flash("LAS CLAVES NO COINCIDEN")
        return redirect(url_for('main.registro'))

    #Verificación de existencia en phpMyAdmin
    user_exists = Usuario.query.filter_by(username=username).first()
    if user_exists:
        flash("ID NO DISPONIBLE: ELIJA OTRO IDENTIFICADOR")
        return redirect(url_for('main.registro'))

    #Escritura en la base de datos
    try:
        nuevo_usuario = Usuario(username=username, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("UNIDAD REGISTRADA: INICIE SESIÓN")
        return redirect(url_for('main.home'))
    except Exception as e:
        db.session.rollback()
        flash("FALLO DE SISTEMA: ERROR AL CREAR REGISTRO")
        return redirect(url_for('main.registro'))

@main_bp.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('main.home'))