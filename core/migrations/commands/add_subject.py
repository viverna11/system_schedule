from django.core.management.base import BaseCommand
from core.models import Subject


class Command(BaseCommand):
    help = "Додавання нового предмета"

    def handle(self, *args, **kwargs):
        name = input("Введіть назву предмета: ")
        description = input("Введіть опис предмета (необов'язково): ")

        if Subject.objects.filter(name=name).exists():
            self.stdout.write(self.style.ERROR(f"Предмет '{name}' вже існує."))
        else:
            Subject.objects.create(name=name, description=description)
            self.stdout.write(self.style.SUCCESS(f"Предмет '{name}' успішно додано."))