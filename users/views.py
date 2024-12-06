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

    def form_valid(self, form):
        """ Отправка подтверждения регистрации на почту """

        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/email-confirm/{token}/'
        send_mail(subject="Потверждение почты", message=f"Рады вашей регистрации!Осталось потвердить почту!{url}",
                  from_email=EMAIL_HOST_USER, recipient_list=[user.email])

        return super().form_valid(form)


def email_verification(request, token):
    """ Изменения статуса пользователя на активный после подтверждения почты """

    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserDetailView(DetailView):
    model = User
    template_name = "detail_user.html"


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "update_user.html"
    success_url = reverse_lazy('users:detail_user')

    def get_success_url(self):
        """ Функция возврата на информацию о пользователе в случае внесения изменений """

        return reverse("users:detail_user", args=[self.kwargs.get('pk')])


def user_logout(request):
    """ Функция выхода с авторизации """

    logout(request)
    return render(request, template_name="main.html")
