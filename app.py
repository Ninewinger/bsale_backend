from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Products, Category

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bsale_test:bsale_test@mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com/bsale_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def get_products():
    product = Products.query.all()
    product = list(map(lambda product: product.serialize(), product))

    return jsonify(product), 200
    
@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Products.query.get(id)
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.serialize()), 200

@app.route('/category', methods=['GET'])
def get_category():
    category = Category.query.all()
    category = list(map(lambda category: category.serialize(), category))

    return jsonify(category)

@app.route('/category/<int:id>', methods=['GET'])
def get_category_by_id(id):
    category = Category.query.get(id)
    if category is None:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(category.get_products()), 200

#search by name
@app.route('/search', methods=['GET'])
def search_by_name():
    name = request.args.get('name')    
    product = Products.query.filter(Products.name.like('%'+name+'%')).all()
    product = list(map(lambda product: product.serialize(), product))

    return jsonify(product)


if __name__ == '__main__':    
    app.run()