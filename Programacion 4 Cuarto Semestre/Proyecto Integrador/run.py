from app import create_app

# Se invoca la función 'create_app' definida en app/__init__.py
# Esta instancia ya contiene los Blueprints registrados y la conexión a la DB
app = create_app()

# Punto de entrada principal del script
if __name__ == '__main__':
    # Inicia el servidor web local de Flask
    # debug=True activa el reinicio automático al detectar cambios en el código 
    # y muestra una consola interactiva en el navegador en caso de errores
    app.run(debug=True)