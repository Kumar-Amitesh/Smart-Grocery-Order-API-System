from flask import Blueprint, request, jsonify

from services.product_service import add_product, get_all_products, update_product,products
from utils.validators import validate_product_data

product_bp = Blueprint("product", __name__)


@product_bp.route("", methods=["POST"])
def create_product():
    data = request.get_json()
    valid, error = validate_product_data(data, products)
    if not valid:
        return jsonify({"error": error}), 400

    product = add_product(data)
    return jsonify(product.__dict__), 201


@product_bp.route("", methods=["GET"])
def list_products():
    return jsonify(get_all_products()), 200


@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product_info(product_id):
    data = request.get_json()
    product = update_product(product_id, data)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product.__dict__), 200
