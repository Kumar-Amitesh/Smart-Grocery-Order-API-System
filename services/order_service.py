from models import Order, OrderItem
from services.product_service import products

orders = []
order_id_counter = 101


def place_order(data):
    global order_id_counter
    items = [OrderItem(**item) for item in data["items"]]
    order = Order(
        order_id=order_id_counter,
        customer_name=data["customer_name"],
        items=items
    )
    orders.append(order)
    order_id_counter += 1
    return order


def get_all_orders():
    result = []
    for order in orders:
        order_dict = {
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "items": [],
            "total_amount": 0
        }
        for item in order.items:
            product = next((p for p in products if p.id == item.product_id), None)
            if product:
                price = product.price_per_unit * item.quantity
                order_dict["items"].append({
                    "product_id": product.id,
                    "product_name": product.name,
                    "quantity": item.quantity,
                    "price": price
                })
                order_dict["total_amount"] += price
        result.append(order_dict)
    return result
