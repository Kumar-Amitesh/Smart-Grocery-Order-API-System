def validate_product_data(data, existing_products):
    if "name" not in data or not isinstance(data["name"], str):
        return False, "Product name is required and must be a string"
    if any(p.name == data["name"] for p in existing_products):
        return False, "Product name must be unique"
    if "price_per_unit" not in data or not isinstance(data["price_per_unit"], (int, float)) or data["price_per_unit"] <= 0:
        return False, "Price must be a positive number"
    if "unit" not in data or not isinstance(data["unit"], str):
        return False, "Unit is required and must be a string"
    return True, None


def validate_order_data(data, existing_products):
    if "customer_name" not in data or not isinstance(data["customer_name"], str):
        return False, "Customer name is required"
    if "items" not in data or not isinstance(data["items"], list):
        return False, "Items must be a list"

    valid_ids = {product.id for product in existing_products}
    for item in data["items"]:
        if "product_id" not in item or item["product_id"] not in valid_ids:
            return False, f"Invalid product_id: {item.get('product_id')}"
        if "quantity" not in item or not isinstance(item["quantity"], int) or item["quantity"] <= 0:
            return False, "Quantity must be a positive integer"
    return True, None
