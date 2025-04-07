from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (LoginView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy
from django.views.decorators.cache import cache_page

from users.apps import UsersConfig
from users.views import (RegisterView, UserDetailView, UserUpdateView,
                         email_verification, user_logout)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', user_logout, name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    path('user/detail/<int:pk>', cache_page(60)(UserDetailView.as_view()), name='detail_user'),
    path('user/update/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),

    path('password_reset/',
         PasswordResetView.as_view(
             template_name="password_reset.html",
             email_template_name="password_reset_email.html",
             success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="password_reset_confirm.html",
             success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
