from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_empresa, name='registrar_empresa'),
    path('login/', views.login_empresa, name='login_empresa'),
    path('dashboard/', views.dashboard_empresa, name='dashboard_empresa'),
    path('adicionar-atracao/', views.adicionar_atracao, name='adicionar_atracao'),
    path('adicionar-pacote/', views.adicionar_pacote, name='adicionar_pacote'),
    path('editar-pacote/<int:pacote_id>/', views.editar_pacote, name='editar_pacote'),
    path('editar-atracao/<int:atracao_id>/', views.editar_atracao, name='editar_atracao'),
    path('editar-empresa/', views.editar_empresa, name='editar_empresa'),
    path('insights-atracao/<int:atracao_id>/', views.insights_atracao, name='insights_atracao'),
    path('insights-pacote/<int:pacote_id>/', views.insights_pacote, name='insights_pacote'),
    path('insights-empresa/', views.insights_empresa, name='insights_empresa'),
]
