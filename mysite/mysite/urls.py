from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('info/', views.info, name='info'),  # Страница информации
    path('articles/', views.articles_detail, name='articles_detail'),  # Страница деталей статей
    path('registration/', views.registration, name='registration'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа в систему
]
