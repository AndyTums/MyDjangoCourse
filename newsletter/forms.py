import datetime

from django.forms import forms, EmailField, CharField, Textarea, DateField
from django.forms import ModelForm, BooleanField
from newsletter.models import Newsletter, Recipient, Message, Try
from django import forms
from django.utils import timezone
from datetime import datetime


class StyleFormMixin:
    """ Стилизуем форму """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
                fild.widget.attrs['style'] = 'background-color: #300; color: #5; border-radius: 10px;'
            else:
                fild.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class RecipientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Message
        fields = ['name', 'text', 'owner']


class TryForm(StyleFormMixin, ModelForm):
    subject = CharField(label="Тема")
    message = CharField(widget=Textarea, label="Сообщение")
    recipients = CharField(widget=Textarea, label="Получатели (через запятую)")

    class Meta:
        model = Try
        fields = ['send_time', 'recipients', 'subject', 'message', 'newsletter', ]


class NewsletterModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = ['start_mail', 'end_mail', 'recipient', ]


class RecipientModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Recipient
        fields = ['email']
