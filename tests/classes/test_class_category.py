import pytest

from src.classes.class_category import Category
from src.classes.class_products import Product


@pytest.mark.parametrize(
    "name, description, products, result",
    [
        ("Тест 1", "Описание 1", [], Category),
        ("Тест 2", "Описание 2", [], Category),
    ],
)
def test_category(name: str, description: str, products: list, result: Category) -> None:
    """
    Тестирование класса Category по заготовленным данным
    :param name: Название
    :param description: Описание
    :param products: Список Product
    :param result: Ожидание от теста
    :return: None
    """

    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category = Category(name, description, [product])

    assert isinstance(category, Category)


def test_category_init() -> None:
    """
    Тестирование Category
    :return: None
    """

    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category = Category("Тест 1", "Описание 1", [product])

    assert category.name == "Тест 1"
    assert category.description == "Описание 1"
    assert category.products == [product]
    assert len(category.products) == 1

    get_first_product = category.products[0]
    assert get_first_product.name == '55" QLED 4K'
    assert get_first_product.description == "Фоновая подсветка"
    assert get_first_product.price == 123000.0
    assert get_first_product.quantity == 7
