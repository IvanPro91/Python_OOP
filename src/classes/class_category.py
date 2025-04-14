from abc import ABC, abstractmethod
from typing import Any

from src.classes.class_products import Product


class BaseCategory(ABC):
    """
    Абстрактный класс с перечислением методов для класса Category и его дочерних классов
    """

    @abstractmethod
    def add_product(self, product: Any) -> Any: ...
    def get_total_cost(self) -> Any: ...


class Category(BaseCategory):
    """Шаблон класса Category"""

    category_count: int = 0
    product_count: int = 0
    __products: list[Product] = []

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1

    @classmethod
    def add_product(cls, product: Any) -> None:
        """Добавление нового продукта"""
        # Проверить продукт на цену и произвести поиск
        if not issubclass(product.__class__, Product):
            raise ValueError("Класс не является наследником основного класса.")

        quantity, price = cls.chk_product(product)
        product.quantity = quantity
        product.price = price

        cls.__products.append(product)
        cls.product_count = product.quantity

    @classmethod
    def chk_product(cls, product: Any) -> tuple[int, Any]:
        """Проверка добавляемых данных"""
        # Проверка на схожесть в имени IN
        quantity = 1
        price = product.price

        # Ищем продукт с таким-же именем
        for all_product in cls.__products:
            if product.name == all_product.name:
                quantity = product.quantity + all_product.quantity

                # Решаем конфликт цен
                if product.price > all_product.price:
                    price = product.price
                else:
                    success_low_price = input(f"Цена товара {product.name} снижена, продолжить?\n")
                    if success_low_price.lower() == "y":
                        price = product.price

        return quantity, price

    def middle_price(self) -> float:
        """Среднее значение цены"""
        price = sum([count.price for count in self.__products])
        try:
            middle = price / len(self.__products)
            return middle
        except ZeroDivisionError:
            pass
        return 0

    @property
    def products(self) -> list:
        """Getter, который возвращает информацию по продуктам"""
        return self.__products

    def __str__(self) -> str:
        """Переопределение магического метода str"""

        return f"{self.name}, количество продуктов: {self.product_count} шт."


class Order(BaseCategory):
    """
    Класс "Заказ", который наследуется от абстрактного класса и получает общие абстрактные методы
    """

    def __init__(self, product: Any) -> None:
        self.product = product

    def add_product(self, product: Any) -> None:
        """Абстрактный метод для добавления нового продукта в заказ"""
        if not isinstance(product, Product):
            raise ValueError("Объект не является экземпляром класса Product.")
        self.product = product

    def get_total_cost(self) -> Any:
        """Абстрактный метод для получения общей стоимости заказа"""
        return self.product.price * self.product.quantity

    def __str__(self) -> str:
        product: Product = self.product
        return product.name
