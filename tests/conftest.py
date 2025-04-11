import pytest

from src.classes.class_category import Category
from src.classes.class_products import Product


@pytest.fixture
def product_phone() -> Product:
    """
    Фикстура для Product
    :return: Product
    """
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def fix_category() -> Category:
    """
    Фикстура для Category
    :return: Category
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Apple iPhone 14 Pro", "128GB, Золотой цвет, 48MP камера", 120000.0, 10)
    product3 = Product("Google Pixel 7 Pro", "128GB, Белый цвет, 50MP камера", 90000.0, 7)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return category1
