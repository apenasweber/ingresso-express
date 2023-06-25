from django.urls import path
from . import views

app_name = 'empresas'
urlpatterns = [
    path('registrar/', views.registrar_empresa, name='registrar_empresa'),
    path('dashboard/', views.dashboard_empresa, name='dashboard_empresa'),
    path('insights/', views.insights_geral, name='insights_geral'),
    path('pacote/criar/', views.criar_pacote, name='criar_pacote'),
    path('atracao/criar/', views.criar_atracao, name='criar_atracao'),
    path('pacote/editar/<int:id>/', views.editar_pacote, name='editar_pacote'),
    path('atracao/editar/<int:id>/', views.editar_atracao, name='editar_atracao'),
    path('pacote/insights/<int:id>/', views.insights_pacote, name='insights_pacote'),
    path('atracao/insights/<int:id>/', views.insights_atracao, name='insights_atracao'),
]
