from django.core.management.base import BaseCommand
from core.models import Class


class Command(BaseCommand):
    help = "Додавання нового класу"

    def handle(self, *args, **kwargs):
        name = input("Введіть назву класу (наприклад, '10-А'): ")
        year = input("Введіть рік навчання: ")

        if Class.objects.filter(name=name).exists():
            self.stdout.write(self.style.ERROR(f"Клас '{name}' вже існує."))
        else:
            Class.objects.create(name=name, year=year)
            self.stdout.write(self.style.SUCCESS(f"Клас '{name}' успішно додано."))