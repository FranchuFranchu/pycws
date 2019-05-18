from django.urls import path, include
from . import views

app_name = 'translations'

urlpatterns = [
    path('', views.list_translations, name='list-all'),
    path('new/', views.new_translation, name='new'),
    path('random/', views.random_translation, name='random'),
    path('view/<uuid:id>/', views.view_translation, name='view'),
]
