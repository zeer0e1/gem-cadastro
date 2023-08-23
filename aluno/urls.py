from django.urls import path
from aluno import views

app_name = 'aluno'

urlpatterns = [
    path('', views.index, name='index'),
]
