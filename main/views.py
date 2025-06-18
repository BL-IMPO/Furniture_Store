from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


# View (Представление)
def index(request) -> HttpResponse:

    context = {
        'title': 'Home',
        'content': 'Furniture store - HOME',
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'About Us',
        'content': 'About Us',
        'text_on_page': "We're a new furniture sore that sells such a great furniture!"
    }

    return render(request, 'main/about.html', context)