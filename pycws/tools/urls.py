from django.urls import path, include
from . import views

app_name = 'tools'

urlpatterns = [
    path('lexicon/', include([
        path('lexibuild/', views.lexibuild, name='lexibuild'),
        # Etc, I'm bored
    ]))
]
