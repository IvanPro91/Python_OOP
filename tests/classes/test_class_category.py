from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.classes.class_category import Category
from src.classes.class_products import Product


def test_category(product_phone: Product) -> None:
    """
    Тестирование класса Category на добавление новой продукции
    """
    category = Category("Категория 1", "Описание 1")
    category.add_product(product_phone)

    assert category.category_count == 1
    assert category.product_count == 1


def test_category_price(capsys: CaptureFixture[str], product_phone: Product) -> None:
    """
    Тестирование проверки добавления продукции с разными ценами
    """
    category = Category("Категория 1", "Описание 1")

    with patch("builtins.input", lambda _: "y"):
        category.add_product(product_phone)
        product_phone.price = 12322
        category.add_product(product_phone)
        read_out = capsys.readouterr()
        assert read_out.out == ""

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
    category = Category("Категория 1", "Описание 1")

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
        category = Category("Категория 1", "Описание 1")
        category.add_product(product_phone)
        assert category.products == (
            "Iphone 15, 210000.0 руб. Остаток: 1 шт.\n"
            "\n"
            "Iphone 15, 11322 руб. Остаток: 72 шт.\n"
            "\n"
            "Iphone 15, 11322 руб. Остаток: 72 шт.\n"
            "\n"
            "Iphone 15, 11322 руб. Остаток: 72 шт.\n"
            "\n"
            "Iphone 15, 11322 руб. Остаток: 72 шт.\n"
            "\n"
            "Iphone 15, 210000.0 руб. Остаток: 20 шт.\n"
            "\n"
            "Iphone 15, 210000.0 руб. Остаток: 20 шт.\n"
            "\n"
            "Iphone 15, 210000.0 руб. Остаток: 20 шт.\n"
            "\n"
            "Iphone 15, 210000.0 руб. Остаток: 20 шт.\n"
            "\n"
            "Iphone 15, 210000.0 руб. Остаток: 20 шт.\n"
            "\n"
            "Iphone 15, 210000.0 руб. Остаток: 28 шт.\n"
        )
