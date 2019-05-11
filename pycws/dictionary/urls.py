from django.urls import path, include
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.view_dict, name='view-dict'),
]
