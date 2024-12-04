from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

from .forms import NewsletterForm, RecipientForm, MessageForm
from .models import Recipient, Message, Newsletter

# def main_page(request):
#     """ Отображение главной страницы """
#     return render(request, 'main.html')


""" Работа с моделями NEWSLETTER """


class NewsletterView(ListView):
    model = Newsletter
    template_name = "main.html"


class NewsletterListView(ListView):
    model = Newsletter
    template_name = "newsletter_html/list.html"


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = "newsletter_html/detail.html"


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = "newsletter_html/create.html"
    success_url = reverse_lazy('newsletter:newsletters')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = "newsletter_html/create.html"
    success_url = reverse_lazy('newsletter:newsletters')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = "newsletter_html/delete.html"
    success_url = reverse_lazy('newsletter:newsletters')


""" Работа с моделями RECIPIENT """


class RecipientListView(ListView):
    model = Recipient
    template_name = "recipient_html/list.html"


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = "recipient_html/detail.html"


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "recipient_html/create.html"
    success_url = reverse_lazy('newsletter:recipient')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "recipient_html/create.html"
    success_url = reverse_lazy('newsletter:recipient')


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = "recipient_html/delete.html"
    success_url = reverse_lazy('newsletter:recipient')


""" Работа с моделями MESSAGE """


class MessageListView(ListView):
    model = Message
    template_name = "message_html/list.html"


class MessageDetailView(DetailView):
    model = Message
    template_name = "message_html/detail.html"


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "message_html/create.html"
    success_url = reverse_lazy('newsletter:message')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "message_html/create.html"
    success_url = reverse_lazy('newsletter:message')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message_html/delete.html"
    success_url = reverse_lazy('newsletter:message')
