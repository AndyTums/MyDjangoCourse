from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
# from .forms import CustomCreationForm
from newsletter.forms import StyleFormMixin
from users.models import User
import secrets
from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = StyleFormMixin
    success_url = reverse_lazy('newsletter:main')
