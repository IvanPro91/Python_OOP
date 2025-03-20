import pytest

from src.classes.class_products import Product


@pytest.mark.parametrize(
    "name, description, price, quantity, result",
    [
        ("Тест 1", "Описание 1", 10, 12, Product),
        ("Тест 2", "Описание 2", 40, 31, Product),
    ],
)
def test_product(name: str, description: str, price: float, quantity: int, result: Product) -> None:
    """
    Тестирование класса Product по заготовленным данным
    :param name: Название
    :param description: Описание
    :param price: Цена
    :param quantity: Остаток
    :param result: Ожидание от теста
    :return: None
    """

    assert type(Product(name, description, price, quantity)) == Product


def test_product_init(product_phone: Product) -> None:
    """
    Тестирование Product при помощи фикстуры
    :param product_phone: Фикстура
    :return: None
    """
    assert product_phone.name == "Iphone 15"
    assert product_phone.description == "512GB, Gray space"
    assert product_phone.price == 210000.0
    assert product_phone.quantity == 8
