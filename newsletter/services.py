from newsletter.models import Recipient, Newsletter, Message
from users.models import User


class GetInfo:

    @staticmethod
    def get_user_newsletter(user_id):
        """ Получаем весь список моделей NEWSLETTER согласно правам доступа """

        newsletter = Newsletter.objects.filter(owner=user_id)

        return newsletter

    @staticmethod
    def get_user_recipient(user_id):
        """ Получаем весь список моделей RECIPIENT согласно правам доступа """

        recipient = Recipient.objects.filter(owner=user_id)

        return recipient
