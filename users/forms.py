from django import forms
from django.contrib.auth.forms import UserCreationForm

from newsletter.forms import StyleFormMixin
from users.models import User


class CustomCreationForm(StyleFormMixin, UserCreationForm):
    """ Форма регистрации пользователя """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'photo')


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    """ Форма редактирования пользователя """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'country', 'photo',)
