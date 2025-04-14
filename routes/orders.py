from flask import Blueprint, request, jsonify

from services.order_service import place_order, get_all_orders
from services.product_service import products
from utils.validators import validate_order_data

order_bp = Blueprint("order", __name__)

@order_bp.route("", methods=["POST"])
def create_order():
    data = request.get_json()
    valid, error = validate_order_data(data, products)
    if not valid:
        return jsonify({"error": error}), 400

    order = place_order(data)
    return jsonify({"order_id": order.order_id}), 201

@order_bp.route("", methods=["GET"])
def list_orders():
    return jsonify(get_all_orders()), 200
