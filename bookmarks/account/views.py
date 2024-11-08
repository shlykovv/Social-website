from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.forms import UserRegistrationForm


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'section': 'dashboard',
    }
    return render(request,
                  'account/dashboard.html',
                  context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создать новый объект пользователя
            # но пока без сохранения
            new_user = user_form.save(commit=False)
            # Установить новый пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохраняем объект
            new_user.save()
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    context = {
        'title': 'Create an account',
        'user_form': user_form,
            }
    return render(request,
                  'account/register.html',
                  context)
