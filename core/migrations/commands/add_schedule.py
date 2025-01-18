from django.core.management.base import BaseCommand
from core.models import Schedule, Subject, Teacher, Class


class Command(BaseCommand):
    help = "Додавання заняття до розкладу"

    def handle(self, *args, **kwargs):
        day_of_week = input("Введіть день тижня (наприклад, 'Понеділок'): ")
        start_time = input("Введіть час початку заняття (формат HH:MM): ")
        subject_name = input("Введіть назву предмета: ")
        class_name = input("Введіть назву класу (наприклад, '10-А'): ")
        teacher_name = input("Введіть ім'я та прізвище вчителя (наприклад, 'Іван Іванов'): ")

        try:
            subject = Subject.objects.get(name=subject_name)
            school_class = Class.objects.get(name=class_name)
            teacher = Teacher.objects.get(first_name=teacher_name.split()[0], last_name=teacher_name.split()[1])
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Предмет '{subject_name}' не знайдено."))
            return
        except Class.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Клас '{class_name}' не знайдено."))
            return
        except Teacher.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Вчителя '{teacher_name}' не знайдено."))
            return

        schedule, created = Schedule.objects.get_or_create(
            day_of_week=day_of_week,
            start_time=start_time,
            subject=subject,
            school_class=school_class,
            teacher=teacher
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Заняття успішно додано до розкладу."))
        else:
            self.stdout.write(self.style.WARNING("Таке заняття вже існує."))