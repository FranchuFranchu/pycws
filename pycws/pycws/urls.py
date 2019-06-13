"""pycws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('', views.feed, name='feed'),
    path('articles/', include('articles.urls')),
    path('boards/', include('boards.urls')),
    path('clans/', include('clans.urls')),
    path('langs/', include('languages.urls')),
    path('tools/', include('tools.urls')),
    path('trans/', include('translations.urls')),
    path('profile/', include('users.urls')),
)
