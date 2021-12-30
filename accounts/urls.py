from .views import http_login,http_logout,http_signup
from django.urls import path
from django.contrib.auth import views as auth_views

# app_name="accounts"

urlpatterns = [
    
    path("login/",http_login,name='login'),
    path("logout/",http_logout,name='logout'),
    path("signup/",http_signup,name='signup'),

    path("reset_password/" , auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html') , name="reset_password"),
    path("reset_password_sent/" , auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_sent.html') , name="password_reset_done"),
    path("reset/<uidb64>/<token>/" , auth_views.PasswordResetConfirmView.as_view(template_name='accounts/set_password.html') , name="password_reset_confirm"),
    path("reset_password_complete/" , auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_completed.html') , name="password_reset_complete"),

]   