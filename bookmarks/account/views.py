from account.forms import ProfileEditForm, UserEditForm, UserRegistrationForm
from account.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'section': 'dashboard',
    }
    return render(request,
                  'account/dashboard.html',
                  context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm()
        messages.info(request, 'Fill in the fields to change')
    context = {
        'title': 'Edit your account',
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'account/edit.html', context)


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
            Profile.objects.create(user=new_user)
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
