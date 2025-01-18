from django.core.management.base import BaseCommand
from core.models import Student, Class


class Command(BaseCommand):
    help = "Додавання нового учня"

    def handle(self, *args, **kwargs):
        first_name = input("Введіть ім'я учня: ")
        last_name = input("Введіть прізвище учня: ")
        class_name = input("Введіть назву класу (наприклад, '10-А'): ")

        try:
            school_class = Class.objects.get(name=class_name)
        except Class.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Клас '{class_name}' не знайдено."))
            return

        student, created = Student.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            school_class=school_class
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Учня '{first_name} {last_name}' додано до класу '{class_name}'."))
        else:
            self.stdout.write(self.style.WARNING(f"Учень '{first_name} {last_name}' вже існує."))