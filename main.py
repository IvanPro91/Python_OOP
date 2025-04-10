from src.classes.class_category import Category
from src.classes.class_iter_item import IterItem
from src.classes.class_products import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Apple iPhone 14 Pro", "128GB, Золотой цвет, 48MP камера", 120000.0, 10)
    product3 = Product("Google Pixel 7 Pro", "128GB, Белый цвет, 50MP камера", 90000.0, 7)
    product4 = Product("OnePlus 11", "256GB, Синий цвет, 48MP камера", 85000.0, 8)
    product5 = Product("Xiaomi Mi 12", "256GB, Черный цвет, 108MP камера", 75000.0, 12)
    product6 = Product("Sony Xperia 1 IV", "256GB, Черный цвет, 12MP камера", 110000.0, 6)
    product7 = Product("Huawei P50 Pro", "256GB, Зеленый цвет, 50MP камера", 95000.0, 9)
    product8 = Product("LG G8 ThinQ", "128GB, Синий цвет, 48MP камера", 60000.0, 15)
    product9 = Product("Motorola Edge 30", "128GB, Красный цвет, 108MP камера", 55000.0, 11)
    product10 = Product("Nokia G50", "128GB, Черный цвет, 50MP камера", 30000.0, 20)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    category2 = Category("Ноутбуки", "Ноутбуки для работы, учебы и развлечений", [product4, product5, product6])

    category3 = Category("Планшеты", "Планшеты для работы, учебы и развлечений", [product7, product8, product9])

    category4 = Category("Умные часы", "Умные часы для отслеживания здоровья и активности", [product10])

    iter_item = IterItem(category1)
    for item in iter_item:
        print(item)

    iter_item = IterItem(category2)
    print(next(iter_item))
    print(next(iter_item))
    print(next(iter_item))
    print(next(iter_item))
