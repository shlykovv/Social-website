from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm


class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'section': 'dashboard'
    }
    return render(request,
                  'account/dashboard.html',
                  context)
