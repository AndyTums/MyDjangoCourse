from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from newsletter.models import Newsletter, Recipient, Message, Try


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
    class Meta:
        model = Try
        fields = ['send_time', 'status', 'newsletter']


class NewsletterModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = ['start_mail', 'end_mail', 'recipient', ]


class RecipientModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Recipient
        fields = ['email']
