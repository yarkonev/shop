from core.models import Category, Product


def create_categories():
    """
    Создает категории и назначает родительские категории.
    """

    category = """id:title:parent
    1:Велосипеды:None
    2:Кастрюли:4
    3:Тарелки:4
    4:Посуда для кухни:5
    5:Товары для дома:None"""

    # Create categories without assigning parent
    categories = {}
    for line in category.split("\n")[1:]:  # Skip the header line
        id, title, parent = line.split(":")
        categories[id] = Category.objects.create(title=title)

    # Update parent for each category
    for id, category in categories.items():
        parent_id = category.parent_id
        if parent_id and parent_id != "None":
            category.parent = categories[parent_id]
            category.save()


def create_products():
    """
    Заполняет категории товарами.
    """

    products = """id:title:category_id:count:cost
    1:Велосипед:1:100:100.50
    2:Кастрюля 1,5л:2:50:1200
    3:Тарелка 25см:3:1000:25
    4:Кастрюля 3л:2:55:300.78"""

    for line in products.split("\n")[1:]:  # Skip the header line
        id, title, category_id, count, cost = line.split(":")
        try:
            category = Category.objects.get(id=category_id)
            Product.objects.create(
                id=id,
                title=title,
                category=category,
                count=int(count),
                cost=float(cost),
            )
        except Category.DoesNotExist:
            print(f"Category with id {category_id} does not exist")
