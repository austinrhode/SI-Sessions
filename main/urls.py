from django.urls import path
from . import views as main_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', main_views.home, name='home'),
    path('home/week/<int:number>/session/', main_views.get_session, name='session'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),
         name='password_reset_complete'),
    path('', main_views.MyLoginView.as_view(), name='login'),
]