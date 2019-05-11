from django.urls import path, include, register_converter
from . import views
from ..pycws import converters as core_converters

app_name = 'languages'

register_converter(core_converters.LangCodeConverter, 'lang')

urlpatterns = [
    path('', views.list_langs, name='list-all'),
    path('new/', views.new_lang, name='new-lang'),
    path('view/<lang:code>/', include([
        path('', views.view_lang, name='view-lang'),
        path('edit/', views.edit_lang, name='edit-lang'),
        path('dict/', include('dictionary.urls'),
        path('phono/', include([
            path('', views.view_phonology, name='view-phonology'),
            path('edit/', views.edit_phonology, name='edit-phonology')
        ])),
        path('ortho/', views.orthography, name='orthography'),
        # Yadda yadda
    ])),
]
