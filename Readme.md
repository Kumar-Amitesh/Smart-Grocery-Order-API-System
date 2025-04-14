# Smart Grocery Order API System

This is a backend service for a Smart Grocery Order API, built using Python and Flask. It allows users to manage products, place orders, and view all orders and products. The system supports basic CRUD operations and validates product and order data.

## Features

- **Product Management**: 
  - Add new products
  - View all products
  - Update product information
  
- **Order Management**:
  - Place an order with multiple products
  - View all orders
  
- **Validation**:
  - Validates product data (name, price, unit) when adding a new product
  - Validates order data (customer name, items, quantities) when placing an order
  
- **Error Handling**:
  - Handles 404 (Resource not found), 405 (Method not allowed), and 500 (Internal server error) errors.

## Technologies

- **Python 3.1.0**
- **Flask**: Web framework
- **Unittest**: For writing and running tests
- **JSON**: For API responses and requests

## Endpoints

### `/products`

- **GET**: Retrieve a list of all products
  - Response: JSON list of products
  - Example: 
    ```json
    [
      {
        "id": 1,
        "name": "Apple",
        "price_per_unit": 10.0,
        "unit": "kg"
      }
    ]
    ```

- **POST**: Add a new product
  - Request body: JSON object with `name`, `price_per_unit`, and `unit`
  - Example:
    ```json
    {
      "name": "Banana",
      "price_per_unit": 12.5,
      "unit": "kg"
    }
    ```
  - Response: JSON object of the created product, including `id`
  - Example:
    ```json
    {
      "id": 2,
      "name": "Banana",
      "price_per_unit": 12.5,
      "unit": "kg"
    }
    ```

### `/orders`

- **GET**: Retrieve a list of all orders
  - Response: JSON list of orders, each with `order_id`, `customer_name`, `items`, and `total_amount`
  - Example:
    ```json
    [
      {
        "order_id": 101,
        "customer_name": "John Doe",
        "items": [
          {
            "product_id": 1,
            "product_name": "Apple",
            "quantity": 2,
            "price": 20.0
          },
          ...
        ],
        "total_amount": 30.0
      },
      ...
    ]
    ```

- **POST**: Place an order
  - Request body: JSON object with `customer_name` and `items` (list of products with `product_id` and `quantity`)
  - Example:
    ```json
    {
      "customer_name": "John Doe",
      "items": [
        {
          "product_id": 1,
          "quantity": 2
        },
        {
          "product_id": 2,
          "quantity": 1
        }
      ]
    }
    ```
  - Response: JSON object containing the `order_id` of the created order
  - Example:
    ```json
    {
      "order_id": 101
    }
    ```

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kumar-Amitesh/Smart-Grocery-Order-API-System.git
   ```

2. **Navigate into the project directory**:
   ```bash
   cd smart-grocery-order-api
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application**:
   ```bash
   python main.py
   ```

   The application will run on `http://localhost:5000`.

## Running Tests

1. To run unit tests for the project, make sure you have a `tests` folder with the relevant test files. Then, run:
   ```bash
   python -m unittest discover tests/
   ```

2. If you want to run tests for a specific file:
   ```bash
   python -m unittest tests.test_product
   ```

## Error Handling

- **404**: Resource not found
- **405**: Method not allowed
- **500**: Internal server error

## Project Structure

```
smart-grocery-order-api/
├── app.py                    # Main entry point
├── routes/                   # Contains API endpoints
│   ├── products.py           # Product routes
│   └── orders.py             # Order routes
├── services/                 # Business logic for products and orders
│   ├── product_service.py    # Functions for product-related logic
│   └── order_service.py      # Functions for order-related logic
├── models/                   # Data models
│   ├── product.py            # Product model
│   └── order.py              # Order model
├── utils/                    # Utility functions
│   └── validators.py         # Input validation functions
├── tests/                    # Unit tests
    ├── test_product.py       # Tests for product functionality
    └── test_order.py         # Tests for order functionality
```
