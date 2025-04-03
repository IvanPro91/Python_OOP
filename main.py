from src.classes.class_category import Category
from src.classes.class_products import Product

if __name__ == "__main__":
    # Реализация домашней работы 14.2

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 120000.0, 5)
    product3 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product4 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )
    category1.add_product(product1)
    print(category1.product_count)
    print(category1.category_count)

    category1.add_product(product2)
    print(category1.product_count)
    print(category1.category_count)

    category1.add_product(product3)
    print(category1.product_count)
    print(category1.category_count)
