from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

from .forms import NewsletterForm
from .models import Recipient, Message, Newsletter

# def main_page(request):
#     """ Отображение главной страницы """
#     return render(request, 'main.html')


""" Работа с моделями NEWSLETTER """


class NewsletterView(TemplateView):
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
    template_name = "main.html"


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = "main.html"


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = "main.html"
