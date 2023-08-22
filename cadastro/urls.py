from django.urls import path
from dashboard import views

app_name = 'cadastro'

urlpatterns = [
    path('cadastro', views.index, name='index'),
]
