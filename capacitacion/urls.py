from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('diagnostico/<int:modulo_id>/', views.diagnostico_modulo, name='diagnostico_modulo'),
]