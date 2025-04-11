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

    def __add__(self, other_product: Any) -> Any:
        """Переопределение магического метода add"""
        if type(self) == type(other_product):
            return self.__price * self.quantity + other_product.__price * other_product.quantity
        else:
            raise TypeError(f"Ошибка сложения классов {self.__class__} и {other_product.__class__}")


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
