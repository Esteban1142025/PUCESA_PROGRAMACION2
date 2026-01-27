from flask import Blueprint, render_template

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def products_index():
    return render_template("Products/index.html")

@product_bp.route('/products/create')
def products_create():
    return render_template("Products/create.html")

@product_bp.route('/products/read')
def products_read():
    return render_template("Products/read.html")

@product_bp.route('/products/update')
def products_update():
    return render_template("Products/update.html")

@product_bp.route('/products/delete')
def products_delete():
    return render_template("Products/delete.html")