import pytest

from src.classes.class_products import Product


@pytest.fixture
def product_phone() -> Product:
    """
    Фикстура для Product
    :return: Product
    """
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
