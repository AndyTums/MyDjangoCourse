from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

from users.models import User
from .forms import NewsletterForm, RecipientForm, MessageForm, NewsletterModeratorForm, RecipientModeratorForm, TryForm
from .models import Recipient, Message, Newsletter, Try
from .services import GetInfo

# def main_page(request):
#     """ Отображение главной страницы """
#     return render(request, 'main.html')


""" Работа с моделями NEWSLETTER """


class NewsletterView(ListView):
    model = Newsletter
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_newsletter"] = Newsletter.objects.filter(status="Запущена").count()
        context["unique_recipient"] = Recipient.objects.distinct().count()

        return context


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    template_name = "newsletter_html/list.html"

    def get_queryset(self):
        """ Выводим список согласно правам доступа """

        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Newsletter.objects.all()
        return Newsletter.objects.filter(owner=user)


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    template_name = "newsletter_html/detail.html"

    def get_queryset(self):
        """ Выводим список согласно правам доступа """

        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Newsletter.objects.all()
        return Newsletter.objects.filter(owner=user)


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = "newsletter_html/create.html"
    success_url = reverse_lazy('newsletter:newsletters')


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = "newsletter_html/create.html"
    success_url = reverse_lazy('newsletter:newsletters')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsletterForm
        if user.has_perm('newsletter.can_edit'):
            return NewsletterModeratorForm
        return PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    template_name = "newsletter_html/delete.html"
    success_url = reverse_lazy('newsletter:newsletters')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.has_perm('newsletter.can_edit'):
            self.object.save()
            return self.object
        raise PermissionDenied


""" Работа с моделями RECIPIENT """


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = "recipient_html/list.html"

    def get_queryset(self):
        """ Выводим список согласно правам доступа """

        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Recipient.objects.all()
        return Recipient.objects.filter(owner=user)


class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient
    template_name = "recipient_html/detail.html"

    def get_queryset(self):
        """ Выводим список согласно правам доступа """

        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Recipient.objects.all()
        return Recipient.objects.filter(owner=user)


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "recipient_html/create.html"
    success_url = reverse_lazy('newsletter:recipient')


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "recipient_html/create.html"
    success_url = reverse_lazy('newsletter:recipient')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return RecipientForm
        if user.has_perm('recipient.can_edit'):
            return RecipientModeratorForm
        raise PermissionDenied


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    template_name = "recipient_html/delete.html"
    success_url = reverse_lazy('newsletter:recipient')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.has_perm('recipient.can_edit'):
            self.object.save()
            return self.object
        raise PermissionDenied


""" Работа с моделями MESSAGE """


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "message_html/list.html"

    def get_queryset(self):
        """ Выводим список согласно правам доступа """

        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Message.objects.all()
        return Message.objects.filter(owner=user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "message_html/detail.html"

    def get_queryset(self):
        """ Выводим список согласно правам доступа """

        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Message.objects.all()
        return Message.objects.filter(owner=user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "message_html/create.html"
    success_url = reverse_lazy('newsletter:message')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "message_html/create.html"
    success_url = reverse_lazy('newsletter:message')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MessageForm
        if user.has_perm('message.can_edit'):
            return MessageForm
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "message_html/delete.html"
    success_url = reverse_lazy('newsletter:message')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.has_perm('message.can_edit'):
            self.object.save()
            return self.object
        raise PermissionDenied


""" Работа с моделями TRY """


class TryListView(LoginRequiredMixin, ListView):
    model = Try
    template_name = "newsletter_html/try_list.html"


class TryCreateView(LoginRequiredMixin, CreateView):
    model = Try
    form_class = TryForm
    template_name = "newsletter_html/try_create.html"
    success_url = reverse_lazy('newsletter:try_list')


class TryUpdateView(LoginRequiredMixin, UpdateView):
    model = Try
    form_class = TryForm
    template_name = "newsletter_html/try_create.html"
    success_url = reverse_lazy('newsletter:try')
