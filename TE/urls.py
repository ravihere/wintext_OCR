from django.urls import path
from . import views
from . import forms
urlpatterns = [
    path('', views.index, name = 'home'),
    path('wintext/', views.wintext, name = 'wintext'),
    path('about/', views.about, name = 'about'),
    path('get_text/', views.get_text, name = 'get_text')
]
