from typing import Any


class Product:
    """Шаблон класса Product"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для price"""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для price"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @staticmethod
    def new_product(name: str, description: str, price: float, quantity: int) -> Any:
        """Добавление нового продукта в класс Product"""
        return Product(name, description, price, quantity)

    def __str__(self) -> str:
        """Переопределение магического метода str"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other_product: "Product") -> float:
        """Переопределение магического метода add"""
        return self.__price * self.quantity + other_product.__price * other_product.quantity
