import pytest

from src.classes.class_category import Category
from src.classes.class_iter_item import IterItem


@pytest.mark.parametrize(
    "result",
    [
        ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."),
        ("Google Pixel 7 Pro, 90000.0 руб. Остаток: 7 шт."),
        ("Apple iPhone 14 Pro, 120000.0 руб. Остаток: 10 шт."),
    ],
)
def test_iter_item(fix_category: Category, result: str) -> None:
    iter_item = IterItem(fix_category)
    assert result in list(iter_item)


def test_next_item(fix_category: Category) -> None:
    iter_item = IterItem(fix_category)
    assert next(iter_item) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert next(iter_item) == "Apple iPhone 14 Pro, 120000.0 руб. Остаток: 10 шт."
    assert next(iter_item) == "Google Pixel 7 Pro, 90000.0 руб. Остаток: 7 шт."
