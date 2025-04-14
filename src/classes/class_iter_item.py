from typing import Any

from src.classes.class_category import Category


class IterItem:
    """Шаблон класса IterItem для итерации по классу Category"""

    def __init__(self, category: Category):
        self.category = category
        self.index: int = 0

    def __iter__(self) -> "IterItem":
        """Переопределение магического метода __iter__"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Переопределение магического метода __next__"""
        if self.index < len(self.category.products):
            result = self.category.products[self.index]
            self.index += 1
            return str(result)
        else:
            raise StopIteration
