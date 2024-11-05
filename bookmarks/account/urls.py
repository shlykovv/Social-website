from django.urls import path
from django.contrib.auth import views as auth_view

from account import views
app_name = 'account'


urlpatterns = [
    # предыдущий url входа
    # path('login/', views.user_login, name='login'),

    # url-адреса входа и выхода
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logged_out'),

    path('', views.dashboard, name='dashboard'),
]