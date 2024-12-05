from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
# from .forms import CustomCreationForm
from newsletter.forms import StyleFormMixin
from users.forms import CustomCreationForm, UserUpdateForm
from users.models import User
import secrets
from config.settings import EMAIL_HOST_USER

""" Работа с моделями MESSAGE """


class RegisterView(CreateView):
    """ Контроллер регистрации пользователя """

    model = User
    template_name = 'register.html'
    form_class = CustomCreationForm
    success_url = reverse_lazy('users:login')


class UserDetailView(DetailView):
    model = User
    template_name = "detail_user.html"


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "update_user.html"
    success_url = reverse_lazy('users:detail_user')


def user_logout(request):
    """ Функция выхода с авторизации """

    logout(request)
    return render(request, template_name="main.html")
