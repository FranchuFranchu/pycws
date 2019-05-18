from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.list_articles, name='list-all'),
    path('lotm/', views.list_articles, name='list-lotm'),  # Pending decision on how article searching works
    path('new/', views.new_article, name='new'),
    path('view/<uuid:id>/', views.view_article, name='view'),
]
