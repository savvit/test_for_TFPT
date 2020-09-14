from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import ModelNameForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.urls import reverse


def registration_view(request):
    form = ModelNameForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Юзер {username} был успешно создан. Войтдите в аккаунт.')
        return redirect('home')

    else:
        form = ModelNameForm()
        # messages.warning(request, f'Введите корректные данные.')

    return render(request, 'users/registration.html', {'form': form})
