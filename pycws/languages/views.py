from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

import languages.forms as langForms
from languages.models import Language
from users.models import UserProfile

# Create your views here.
def list_langs(request):
    langs = Language.objects.all()
    return render(request, 'languages/list.html', {'langs': langs})

def view_lang(request, code):
    lang = Language.objects.filter(code=code).first()
    return render(request, 'languages/view.html', {'lang': lang})

def edit_lang(request, code):
    lang = Language.objects.filter(code=code).first()
    # Check if current user is owner of this lang
    profile = UserProfile.objects.filter(user=request.user).first()
    if lang.profile == profile:
        form = langForms.LanguageForm(request.POST or None, instance = lang)

        if form.is_valid():
            form.save(commit=False)
            redirect('/')

        context = {'form': form}
        return render(request, 'languages/edit.html', context)
    response403 = HttpResponse()
    response403.status_code = 403
    return response403

def new_lang(request):
    form = langForms.LanguageForm(request.POST or None)

    if form.is_valid():
        new_language_model = form.save(commit=False)

        # Get profile corresponding to the current user
        corresponding_profile = UserProfile.objects.filter(user=request.user)
        new_language_model.profile = corresponding_profile.first()
        new_language_model.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'languages/new.html', context)

def view_phonology(request, code):
    raise Http404

def edit_phonology(request, code):
    raise Http404

def orthography(request, code):
    raise Http404
