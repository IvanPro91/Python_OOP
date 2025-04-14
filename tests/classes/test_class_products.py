import pytest
from _pytest.capture import CaptureFixture

from src.classes.class_category import Category
from src.classes.class_products import LawnGrass, Product, Smartphone


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


def test_setter_price(capsys: CaptureFixture[str], product_phone: Product) -> None:
    """
    Тестирование сеттера price
    :param product_phone: Фикстура
    :return: None
    """
    product_phone.price = -1
    read_out = capsys.readouterr()
    assert read_out.out == (
        "Создан объект класса Product с параметрами: name='Iphone 15' "
        "description='512GB, Gray space' price=210000.0 quantity=8\n"
        "Цена не должна быть нулевая или отрицательная\n"
    )


def test_new_product() -> None:
    """
    Тестирование создания нового продукта с помощью статического метода
    :return: None
    """
    data_product = Product.new_product("Название продукта", "Описание", 100, 1)
    assert data_product.name == "Название продукта"
    assert data_product.description == "Описание"
    assert data_product.price == 100
    assert data_product.quantity == 1


def test_price_zero_count() -> None:
    """
    Тестирование на инициализацию продукта с нулевым остатком
    """
    with pytest.raises(ValueError):
        Product("Продукт1", "Описание продукта", 1200, 0)


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


def test_add_product() -> None:
    """
    Тестирование переопределения метода add
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Apple iPhone 14 Pro", "128GB, Золотой цвет, 48MP камера", 120000.0, 10)
    res = product1 + product2
    assert res == 2100000.0


def test_raise_add_product() -> None:
    """
    Тестирование ошибок raise для метода сложения
    """
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_other_add_product() -> None:
    """
    Тестирование ошибок на добавление других товаров
    """
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [])
    with pytest.raises(ValueError):
        category_smartphones.add_product("Not a product")
