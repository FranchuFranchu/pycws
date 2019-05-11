from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404

def feed(request):
    return render(request, 'feed.html')
