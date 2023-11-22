from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Категория товара. Содержит название и родительские категории."""

    title = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    """Товар. Содержит название, категорию, количество и цену."""

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    count = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100000)]
    )
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def get_categories(self) -> str:
        """Возвращает категорию товара и ее родительские категории."""

        category_path = [self.category.title]
        parent_category = self.category.parent
        while parent_category != None:
            category_path.append(parent_category.title)
            parent_category = parent_category.parent
        return " · ".join(reversed(category_path))

    def __str__(self) -> str:
        return self.title
