from datetime import timezone

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from config.settings import CACHE_ENABLE
# from newsletter.forms import TryForm
from newsletter.models import Recipient, Newsletter, Message
from users.models import User


def get_newsletter_from_cache():
    """ Низкоуровневое кэширование NEWSLETTER """

    if not CACHE_ENABLE:
        return Newsletter.objects.all()
    key = "newsletter_list"
    info_cache = cache.get(key)
    if info_cache is not None:
        return info_cache
    info_cache = Newsletter.objects.all()
    cache.set(key, info_cache)
    return info_cache


def get_recipient_from_cache():
    """ Низкоуровневое кэширование RECIPIENT """

    if not CACHE_ENABLE:
        return Recipient.objects.all()
    key = "products_list"
    info_cache = cache.get(key)
    if info_cache is not None:
        return info_cache
    info_cache = Recipient.objects.all()
    cache.set(key, info_cache)
    return info_cache


def get_message_from_cache():
    """ Низкоуровневое кэширование MESSAGE """

    if not CACHE_ENABLE:
        return Message.objects.all()
    key = "message_list"
    info_cache = cache.get(key)
    if info_cache is not None:
        return info_cache
    info_cache = Message.objects.all()
    cache.set(key, info_cache)
    return info_cache


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

# def send_email(request):
#     if request.method == "POST":
#         form = TryForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["subject"]
#             message = form.cleaned_data["message"]
#             recipients = form.cleaned_data["recipients"].split(",")
#
#             # Отправка письма всем получателям
#             send_mail(
#                 subject,
#                 message,
#                 'andyqqqq@yandex.ru',
#                 recipients,
#                 fail_silently=False,
#             )
#             return HttpResponse("Рассылка отправлена!")
#     else:
#         form = TryForm()
#
#     return render(request, "newsletter_html/try_create.html", {"form": form})
