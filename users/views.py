from django.shortcuts import render


def login(request):
    context = {
        'title': 'Home - upoważnienie',
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - rejestracja',
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - profil',
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass
