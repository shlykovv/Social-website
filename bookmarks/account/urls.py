from django.contrib.auth import views as auth_view
from django.urls import path, reverse_lazy

from account import views

app_name = 'account'


urlpatterns = [
    # предыдущий url входа
    # path('login/', views.user_login, name='login'),

    # url-адреса входа и выхода
    path('login/',
         auth_view.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_view.LogoutView.as_view(),
         name='logged_out'),
    path('edit/', views.edit, name='edit'),

    # url-адрес смены пароля
    path('password-change/',
         auth_view.PasswordChangeView.as_view(
             success_url=reverse_lazy(
                 'account:password_change_done')
         ),
         name='password_change'),
    path('password-change/done/',
         auth_view.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # url-адреса сброса пароля
    path('password-reset/',
         auth_view.PasswordResetView.as_view(
             success_url=reverse_lazy(
                 'account:password_reset_done')
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>',
         auth_view.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy(
                 'account:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('password-reset/complete',
         auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # path('', include('django.contrib.auth.urls')),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register')
]
