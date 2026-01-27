from flask import Flask
from flask import render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<p>Hello, World!</p>"

# @app.route("/bienvenida")
# def bienvenida():
#     return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/xyz")
def xyz():
    return render_template("xyz.html")

@app.route("/user")
def user_index():
    return render_template("usuarios/index.html")

@app.route("/category")
def category_index():
    return render_template("categorias/index.html")



@app.route("/product")
def product_index():
    return render_template("productos/index.html")

@app.route("/create_product")
def product_create():
    return render_template("productos/create.html")

@app.route("/update_product")
def product_update():
    return render_template("productos/update.html")

@app.route("/delete_product")
def product_delete():
    return render_template("productos/delete.html")





@app.route("/saludos/<nombre>")
def saludo(nombre):
    return f"hola {nombre}, bievenido a Flask"

if __name__ == "__main__":
    app.run(debug=True)