from django.core.management.base import BaseCommand
from core.utils import create_categories, create_products


class Command(BaseCommand):
    help = "Fills the database with data"

    def handle(self, *args, **options):
        create_categories()
        create_products()
        self.stdout.write(self.style.SUCCESS("Database filled successfully"))
