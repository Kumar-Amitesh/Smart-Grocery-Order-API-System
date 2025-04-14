import unittest
from main import app
from services.product_service import products


class ProductTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method will run once before all tests
        cls.app = app.test_client()
        cls.app.testing = True

    def setUp(self):
        # This method will run before every individual test
        global products
        products = []  # Clear the products list before each test

    def test_create_product_success(self):
        new_product = {
            "name": "Apple",
            "price_per_unit": 2.5,
            "unit": "kg"
        }
        response = self.app.post("/products", json=new_product)
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Apple")
        self.assertEqual(data["price_per_unit"], 2.5)

    def test_create_product_name_required(self):
        new_product = {
            "price_per_unit": 2.5,
            "unit": "kg"
        }
        response = self.app.post("/products", json=new_product)
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Product name is required and must be a string")

    def test_create_product_price_required(self):
        new_product = {
            "name": "Apple",
            "unit": "kg"
        }
        response = self.app.post("/products", json=new_product)
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Price must be a positive number")

    def test_create_product_unique_name(self):
        new_product_1 = {
            "name": "Apple",
            "price_per_unit": 2.5,
            "unit": "kg"
        }
        new_product_2 = {
            "name": "Apple",  # Same name should fail
            "price_per_unit": 3.0,
            "unit": "kg"
        }

        # Adding first product
        self.app.post("/products", json=new_product_1)

        # Adding second product with duplicate name
        response = self.app.post("/products", json=new_product_2)
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Product name must be unique")


if __name__ == "__main__":
    unittest.main()
