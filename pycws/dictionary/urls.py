from django.urls import path, include
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.view_dict, name='view-dict'),
    path('new_word/', views.new_word, name='new-word'),
    path('word/<lemma>/', include([
        path('', views.view_word, name='view-word'),
        path('edit/', views.edit_word, name='edit-word'),
        path('delete/', views.delete_word, name='delete-word'),
        path('<int:hnum>/', include([
            path('', views.view_word, name='view-word-hnym'),
            path('edit/', views.edit_word, name='edit-word-hnym'),
            path('delete/', views.delete_word, name='delete-word-hnym'),
        ])),
    ])),
    path('settings/', views.settings, name='settings'),
    path('import/', views.import_dict, name='import'),
    path('export/', views.export_dict, name='export'),
    path('mass_edit/', views.mass_edit, name='mass-edit'),
    path('auto_match/', views.auto_match, name='auto-match'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('purge/', views.purge, name='purge'),
    path('homonyms/', views.homonyms, name='homonyms'),
    path('classes/', include([
        path('', views.classes, name='classes'),
        path('distribution/', views.class_distribution, name='class-distribution'),
    ])),
    path('roots/', views.roots, name='roots'),
]
