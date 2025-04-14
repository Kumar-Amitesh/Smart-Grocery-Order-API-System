from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    price_per_unit: float
    unit: str
    id: int = None

@dataclass
class OrderItem:
    product_id: int
    quantity: int
    product_name: str = None
    price: float = None

@dataclass
class Order:
    customer_name: str
    items: List[OrderItem]
    order_id: int = None
    total_amount: float = None