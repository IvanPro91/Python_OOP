from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

from src.classes.class_category import Category, Order
from src.classes.class_products import Product


def test_category(product_phone: Product) -> None:
    """
    Тестирование класса Category на добавление новой продукции
    """
    category = Category("Категория 1", "Описание 1", [])
    category.add_product(product_phone)

    assert category.category_count == 1
    assert category.product_count == 1


def test_category_price(capsys: CaptureFixture[str], product_phone: Product) -> None:
    """
    Тестирование проверки добавления продукции с разными ценами
    """
    category = Category("Категория 1", "Описание 1", [])

    with patch("builtins.input", lambda _: "y"):
        category.add_product(product_phone)
        product_phone.price = 12322
        category.add_product(product_phone)
        read_out = capsys.readouterr()
        assert read_out.out == (
            "Создан объект класса Product с параметрами: name='Iphone 15' "
            "description='512GB, Gray space' price=210000.0 quantity=8\n"
        )

    with patch("builtins.input", lambda _: "n"):
        category.add_product(product_phone)
        product_phone.price = 11322
        category.add_product(product_phone)
        read_out = capsys.readouterr()
        assert read_out.out == ""


def test_category_quantity(capsys: CaptureFixture[str], product_phone: Product) -> None:
    """
    Тестирование проверки добавления продукции по количеству
    """
    category = Category("Категория 1", "Описание 1", [])

    with patch("builtins.input", lambda _: "y"):
        category.add_product(product_phone)
        product_phone.quantity = 10
        category.add_product(product_phone)
        category.add_product(product_phone)
        assert category.product_count == 40

    with patch("builtins.input", lambda _: "n"):
        category.add_product(product_phone)
        product_phone.quantity = 10
        category.add_product(product_phone)
        assert category.product_count == 20


def test_get_products(product_phone: Product) -> None:
    """
    Тестирование проверки добавления продукции по количеству
    """
    with patch("builtins.input", lambda _: "y"):
        category = Category("Категория 1", "Описание 1", [])
        category.add_product(product_phone)
        assert category.products == []


def test_str_category(fix_category: Category) -> None:
    """
    Тестирование переопределения метода str
    """
    assert isinstance(str(fix_category), str)


def test_middle_price_category() -> None:
    """
    Тестирование средней цены
    """
    category = Category("Категория 1", "Описание 1", [])
    middle_price = category.middle_price()
    assert middle_price == 0


def test_order_abs_category(fix_category: Category) -> None:
    """
    Тестирование переопределения метода str
    """
    product1 = Product("Продукт1", "Описание продукта", 1200, 10)
    product2 = Product("Продукт2", "Описание продукта", 800, 5)

    # Создание категории и добавление продуктов
    category = Category("Категория1", "Описание категории", [])
    category.add_product(product1)
    category.add_product(product2)
    print(category)

    order = Order(product1)
    assert str(order) == "Продукт1"
    assert order.get_total_cost() == 1200

    order.add_product(product2)

    with pytest.raises(ValueError):
        order.add_product("Не продукт")
