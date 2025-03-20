from src.classes.class_products import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products
        self.category_count += 1
        self.product_count += len(products)
