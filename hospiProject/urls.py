"""hospiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paciente/', views.PacienteCrearView.as_view()), 
    path('pacienteTodos/', views.PacienteTodosView.as_view()),  
    path('medico/', views.MedicoCrearView.as_view()),
    path('medicoTodos/', views.MedicoTodosView.as_view()),
    path('pacienteDetalle/<int:pk>', views.PacienteDetalleView.as_view()),
    path('pacienteCambiarMedico/<int:pk>/', views.PacienteCambiarMedicoView.as_view()),
    path('pacienteMedicoView/<medico>', views.PacienteMedicoView.as_view()),
    path('familiarDesignadoView/', views.FamiliarDesignadoTodosView.as_view()),
    path('signoVitalTodos/', views.SignoVitalTodosView.as_view()),
    
]
