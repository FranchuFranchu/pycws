from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
]
