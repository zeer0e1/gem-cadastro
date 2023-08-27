from django.urls import path
from aluno import views
from django.contrib.admin.views.decorators import staff_member_required
app_name = 'aluno'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='dashboard'),
    path('search/', views.search, name='search'),

    path('alunos/', views.about, name='about-us'),

    path('<int:aluno_id>/', views.aluno, name='aluno'),


    # aluno CRUD
    path('aluno/<int:aluno_id>/detail',
         staff_member_required(views.aluno), name='aluno'),
    path('aluno/create/', staff_member_required(views.create), name='create'),
    path('aluno/<int:aluno_id>/update',
         staff_member_required(views.update), name='update'),
    path('aluno/<int:aluno_id>/delete',
         staff_member_required(views.delete), name='delete'),


    # user
    path('user/create/', views.register, name='register'),


    # login
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update', views.user_update, name='user_update'),


]
