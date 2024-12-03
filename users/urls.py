from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from django.conf import settings
from django.conf.urls.static import static
# from .views import RegisterView, email_verification, user_logout

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', user_logout, name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('email-confirm/<str:token>/', email_verification, name='email-confirm'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
