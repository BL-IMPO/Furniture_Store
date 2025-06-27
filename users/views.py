from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Pomyślnie zalogowałeś się na swoje konto.")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - upoważnienie',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Rejestracja i logowanie na koncie przebiegły pomyślnie.")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - rejestracja',
        'form': form,
    }

    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil zaktualizowano pomyślnie")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - profil',
        'form': form,
    }

    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')



@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Pomyślnie wylogowałeś się ze swojego konta.")
    auth.logout(request)
    return redirect(reverse('main:index'))
