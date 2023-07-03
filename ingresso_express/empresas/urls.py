from django.urls import path, include
from . import views

app_name = "empresas"

urlpatterns = [
    path("registrar/", views.registrar_empresa, name="registrar_empresa"),
    path("dashboard/", views.dashboard_empresa, name="dashboard_empresa"),
    path("editar/", views.editar_empresa, name="editar_empresa"),
    path("login/", views.login_empresa, name="login"),
]
