from django.urls import path
from aluno import views

app_name = 'aluno'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='dashboard'),
    path('search/', views.search, name='search'),

    path('alunos/', views.about, name='about-us'),
    
    path('<int:aluno_id>/', views.aluno, name='aluno'),
    
    
    # aluno CRUD
    path('aluno/<int:aluno_id>/detail', views.aluno, name='aluno'),
    path('aluno/create/', views.create, name='create'),
   

]
