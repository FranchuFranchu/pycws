from django.shortcuts import render
from django.http import Http404

# The dictionary views must include an argument `code` for the language code

# Create your views here.
def view_dict(request, code):
    raise Http404

def new_word(request, code):
    raise Http404

def view_word(request, code, lemma, hnum=0):
    raise Http404

def edit_word(request, code, lemma, hnum=0):
    raise Http404

def delete_word(request, code, lemma, hnum=0):
    raise Http404

def settings(request, code):
    raise Http404

def import(request, code):
    raise Http404

def export(request, code):
    raise Http404

def mass_edit(request, code):
    raise Http404

def auto_match(request, code):
    raise Http404

def maintenance(request, code):
    raise Http404

def purge(request, code):
    raise Http404

def homonyms(request, code):
    raise Http404

def classes(request, code):
    raise Http404

def class_distribution(request, code):
    raise Http404

def roots(request, code):
    raise Http404
