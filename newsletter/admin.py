from django.contrib import admin
from newsletter.models import Recipient, Message, Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("id", "start_mail", "end_mail", "status", "message")
    list_filter = ("start_mail",)
    search_fields = ("status", "recipient", "start_mail", "end_mail")


@admin.register(Recipient)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "fio", "comment")


@admin.register(Message)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("name", "text")
