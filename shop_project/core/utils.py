from core.models import Category, Product

# Функции для заполнения базы данных


def create_categories():
    """
    Создает категории.
    """

    category = """id:title:parent
    1:Велосипеды:None
    2:Кастрюли:4
    3:Тарелки:4
    4:Посуда для кухни:5
    5:Товары для дома:None"""

    # Разбиение на строки с пропуском первой строки
    lines = category.splitlines()[1:]

    # Создание категорий в базе данных.
    # Цикл проходит в обратном порядке, от крупных категорий к меньшим.
    for line in reversed(lines):
        id, title, parent = line.split(":")
        parent_category = None
        if parent != "None":
            parent_category = Category.objects.get(id=parent)
        Category.objects.create(
            id=id,
            title=title,
            parent=parent_category,
        )


def create_products():
    """
    Заполняет категории товарами.
    """

    products = """id:title:category_id:count:cost
    1:Велосипед:1:100:100.50
    2:Кастрюля 1,5л:2:50:1200
    3:Тарелка 25см:3:1000:25
    4:Кастрюля 3л:2:55:300.78"""

    # Разбиение на строки с пропуском первой строки
    lines = products.splitlines()[1:]

    # Заполнение категорий в базе данных
    for line in lines:
        id, title, category_id, count, cost = line.split(":")
        category = Category.objects.get(id=category_id)
        Product.objects.create(
            id=id,
            title=title,
            category=category,
            count=int(count),
            cost=float(cost),
        )
