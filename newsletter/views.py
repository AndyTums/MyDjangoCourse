from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

from .forms import NewsletterForm
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
    form_class = NewsletterForm
    template_name = "recipient_html/create.html"
    success_url = reverse_lazy('newsletter:newsletters')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = NewsletterForm
    template_name = "recipient_html/create.html"
    success_url = reverse_lazy('newsletter:newsletters')


class RecipientDeleteView(DeleteView):
    model = Newsletter
    template_name = "recipient_html/delete.html"
    success_url = reverse_lazy('newsletter:newsletters')
