from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
]
