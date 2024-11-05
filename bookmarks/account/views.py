from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'section': 'dashboard'
    }
    return render(request,
                  'account/dashboard.html',
                  context)
