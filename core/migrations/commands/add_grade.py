from django.core.management.base import BaseCommand
from core.models import Grade, Student, Subject

class Command(BaseCommand):
    help = "Додавання оцінки"

    def handle(self, *args, **kwargs):
        student_name = input("Введіть ім'я та прізвище учня (наприклад, 'Петро Петренко'): ")
        subject_name = input("Введіть назву предмета: ")
        grade_value = input("Введіть оцінку: ")
        date = input("Введіть дату оцінки (формат YYYY-MM-DD): ")

        try:
            student = Student.objects.get(first_name=student_name.split()[0], last_name=student_name.split()[1])
            subject = Subject.objects.get(name=subject_name)
        except Student.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Учня '{student_name}' не знайдено."))
            return
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Предмет '{subject_name}' не знайдено."))
            return

        grade, created = Grade.objects.get_or_create(
            student=student,
            subject=subject,
            grade=grade_value,
            date=date
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Оцінку '{grade_value}' для учня '{student_name}' додано."))
        else:
            self.stdout.write(self.style.WARNING("Така оцінка вже існує."))