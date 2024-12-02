from django.urls import path
from django.conf import settings
from newsletter.apps import NewsletterConfig
from django.conf.urls.static import static
from newsletter.views import NewsletterView, NewsletterListView, NewsletterDetailView, NewsletterCreateView, \
    NewsletterDeleteView, NewsletterUpdateView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterView.as_view(), name="main"),
    path('newsletters/', NewsletterListView.as_view(), name="newsletters"),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name="detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
