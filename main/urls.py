from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutUsView.as_view(), name='about'),
]
