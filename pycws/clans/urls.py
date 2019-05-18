from django.urls import path, include
from . import views

app_name = 'clans'

urlpatterns = [
    path('', views.list_clans, name='list-all'),
    path('new/', views.new_clan, name='new'),
    path('view/<uuid:id>/', views.view_clan, name='view'),
]
