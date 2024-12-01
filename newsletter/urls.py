from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from newsletter.views import NewsletterView
from newsletter.apps import NewsletterConfig

app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterView.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
