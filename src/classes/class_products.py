from typing import Any


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @staticmethod
    def new_product(name: str, description: str, price: float, quantity: int) -> Any:
        return Product(name, description, price, quantity)
