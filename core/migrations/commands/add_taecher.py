from django.core.management.base import BaseCommand
from core.models import Teacher, Subject

class Command(BaseCommand):
    help = "Додавання нового вчителя"

    def handle(self, *args, **kwargs):
        first_name = input("Введіть ім'я вчителя: ")
        last_name = input("Введіть прізвище вчителя: ")
        subject_name = input("Введіть назву предмета, який викладає вчитель: ")

        try:
            subject = Subject.objects.get(name=subject_name)
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Предмет '{subject_name}' не знайдено."))
            return

        teacher, created = Teacher.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            subject=subject
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Вчителя '{first_name} {last_name}' додано."))
        else:
            self.stdout.write(self.style.WARNING(f"Вчитель '{first_name} {last_name}' вже існує."))