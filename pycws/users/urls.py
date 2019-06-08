from django.urls import path, include, register_converter
from . import views
from pycws import converters

app_name = 'users'

register_converter(converters.UserIDConverter, 'user')

urlpatterns = [
    path('', views.view_profile, name='view-self'),
    path('edit/', views.edit_profile, name='edit-self'),
    path('messages/', include([
        path('', views.list_messages, name='list-messages'),
        path('view/<uuid:id>/', views.view_message, name='view-message'),
        path('send/', include([
            path('', views.send_message, name='send-message'),
            path('<user:id>/', views.send_message, name='send-message-to'),
        ])),
    ])),
    path('view/<user:id>/', views.view_profile, name='view-profile'),
]
