from django.shortcuts import render
from django.http import Http404

# Create your views here.
def list_articles(request):
    raise Http404

def new_article(request):
    raise Http404

def view_article(request, id):
    raise Http404
