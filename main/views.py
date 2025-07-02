from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from goods.models import Categories


# View (Представление)

class IndexView(TemplateView):

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['content'] = 'Furniture store - HOME'

        return context


class AboutUsView(TemplateView):

    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['content'] = 'About Us'
        context['text_on_page'] = "We're a new furniture sore that sells such a great furniture!"

        return context


#def index(request) -> HttpResponse:
#
#    context = {
#        'title': 'Home',
#        'content': 'Furniture store - HOME',
#    }
#
#    return render(request, 'main/index.html', context)


#def about(request) -> HttpResponse:
#    context = {
#        'title': 'About Us',
#        'content': 'About Us',
#        'text_on_page': "We're a new furniture sore that sells such a great furniture!"
#    }
#
#    return render(request, 'main/about.html', context)


