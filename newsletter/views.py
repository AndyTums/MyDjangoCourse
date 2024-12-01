from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View
from .models import Recipient, Message, Newsletter


class NewsletterView(ListView):
    model = Newsletter
    template_name = "base.html"
