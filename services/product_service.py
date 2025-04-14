from models import Product

products = []
product_id_counter = 1


def add_product(data):
    global product_id_counter
    product = Product(id=product_id_counter, **data)
    products.append(product)
    product_id_counter += 1
    return product


def get_all_products():
    return [p.__dict__ for p in products]


def update_product(product_id, data):
    for product in products:
        if product.id == product_id:
            for key, value in data.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            return product
    return None
