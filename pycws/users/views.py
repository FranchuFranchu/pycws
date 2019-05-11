from django.shortcuts import render
from django.http import Http404

# Create your views here.
def view_profile(request, id=''):
    raise Http404

def edit_profile(request):
    raise Http404

def list_messages(request):
    raise Http404

def view_message(request, id):
    raise Http404

def send_message(request, id=''):
    raise Http404
