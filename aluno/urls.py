from django.urls import path
from dashboard import views

app_name = 'aluno'

urlpatterns = [
    path('aluno', views.index, name='index'),
]
