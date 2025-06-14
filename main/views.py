from django.shortcuts import render
from django.http import HttpResponse


# View (Представление)
def index(request) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': 'Main page of the store by the name HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True,
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')