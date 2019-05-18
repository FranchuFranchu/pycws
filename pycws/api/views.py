from django.shortcuts import render
from django.http import Http404

def get_user(request, username):
    raise Http404

def get_lang(request, code):
    raise Http404

def get_lang_status(request, code):
    raise Http404

def get_lang_type(request, code):
    raise Http404
