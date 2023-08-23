from django.urls import path
from aluno import views

app_name = 'aluno'

urlpatterns = [
    path('index.html/', views.index, name='index'),
    path('about-us.html/', views.about, name='about-us'),
    path('<int:aluno_id>/', views.aluno, name='aluno'),
    path('search/', views.search, name='search'),

]
