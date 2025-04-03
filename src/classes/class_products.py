from typing import Any


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.product_price = price
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.product_price

    @price.setter
    def price(self, price: float) -> None:
        if price > 0:
            self.product_price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @staticmethod
    def new_product(name: str, description: str, price: float, quantity: int) -> Any:
        return Product(name, description, price, quantity)
