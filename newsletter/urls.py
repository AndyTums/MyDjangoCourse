from django.urls import path
from django.conf import settings
from newsletter.apps import NewsletterConfig
from django.conf.urls.static import static
from newsletter.views import NewsletterView, NewsletterListView, NewsletterDetailView, NewsletterCreateView, \
    NewsletterDeleteView, NewsletterUpdateView, RecipientDeleteView, RecipientCreateView, RecipientListView, \
    RecipientUpdateView, RecipientDetailView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterView.as_view(), name="main"),
    path('newsletters/', NewsletterListView.as_view(), name="newsletters"),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name="detail"),
    path('create/', NewsletterCreateView.as_view(), name="create"),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name="delete"),

    path('recipient/', RecipientListView.as_view(), name="recipient"),
    path('recipient/create/', RecipientCreateView.as_view(), name="create_recipient"),
    path('recipient/detail/<int:pk>/', RecipientDetailView.as_view(), name="detail_recipient"),
    path('recipient/update/<int:pk>/', RecipientUpdateView.as_view(), name="update_recipient"),
    path('recipient/delete/<int:pk>/', RecipientDeleteView.as_view(), name="delete_recipient"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
