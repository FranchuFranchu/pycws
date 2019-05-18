from django.urls import path, include, register_converter
from languages import converters as langconverters
from . import views

app_name = 'api'

register_converter(langconverters.LangCodeConverter, 'lang')

urlpatterns = [
    path('USER/<username>', views.get_user, name='user'),
    path('LANG/', include([
        path('<lang:code>', views.get_lang, name='lang'),
        path('STATUS/<int:id>', views.get_lang_status, name='lang-status'),
        path('TYPE/<id>', views.get_lang_type, name='lang-type'),
    ]))
]
