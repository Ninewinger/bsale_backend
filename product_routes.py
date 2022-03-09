from flask import Blueprint, jsonify, request

route_products = Blueprint('route_products', __name__)

@route_products.route('/products', methods=['GET'])
def get_products():
    product = Products.query.all()
    product = list(map(lambda product: product.serialize(), product))

    return jsonify(product), 200
    
@route_products.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Products.query.get(id)
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.serialize()), 200