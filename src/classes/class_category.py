from typing import Any

from src.classes.class_products import Product


class Category:
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

    @property
    def products(self) -> list:
        """Getter, который возвращает информацию по продуктам"""
        return self.__products

    def __str__(self) -> str:
        """Переопределение магического метода str"""
        all_cout = sum([count.quantity for count in self.__products])
        return f"{self.name}, количество продуктов: {all_cout} шт."
