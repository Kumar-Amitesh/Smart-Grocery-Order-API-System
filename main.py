from flask import Flask, jsonify
from routes.products import product_bp
from routes.orders import order_bp

# Create Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(order_bp, url_prefix='/orders')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


# Root endpoint
@app.route('/')
def index():
    return jsonify({
        "message": "Smart Grocery Order API System",
        "endpoints": {
            "products": "/products",
            "orders": "/orders"
        }
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)