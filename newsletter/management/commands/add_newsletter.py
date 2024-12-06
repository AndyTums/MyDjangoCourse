from django.core.management import BaseCommand

from newsletter.models import Recipient


class Command(BaseCommand):
    help = "Добавляем рассылку в БД"

    def handle(self, *args, **kwargs):
        recipient_1 = Recipient.objects.create(name="Работа", fio="Папа О.В")

        # message_1 = Message.objects.get_or_create(name="По работе", fio="Работа очень сложна")
        # newsletter_1 = Newsletter.objects.get_or_create(start_mail="2024-01-01", end_mail="2024-02-02",
        #                                                 message=message_1, recipient=recipient_1)
        recipient_1.save()
        # message_1.save()
        # newsletter_1.save()
        pass
