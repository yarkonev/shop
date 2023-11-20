from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Категория товара.
    Содержит название и родительские категории."""

    title = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """Товар.
    Содержит название, категорию, количество и цену."""

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    count = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100000)]
    )
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def get_categories_path(self):
        """
        Возвращает категорию товара и все родительские категории.

        :return: The path of categories for the current category, joined by " · ".
        :rtype: str
        """
        category_path = [self.category.title]
        current_category = self.category.parent
        while current_category is not None:
            category_path.append(current_category.title)
            current_category = current_category.parent
        return " · ".join(reversed(category_path))

    def __str__(self):
        return self.title
