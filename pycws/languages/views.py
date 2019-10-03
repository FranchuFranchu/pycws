from django.shortcuts import render, redirect
from django.http import Http404
import languages.forms as langForms
from users.models import UserProfile
from .models import Language

# Create your views here.
def list_langs(request):
    langs = Language.objects.all()
    return render(request, 'languages/list.html', {'langs': langs})

def view_lang(request, code):
    lang = Language.objects.filter(code=code).get(pk=1)
    return render(request, 'languages/view.html', {'lang': lang})

def edit_lang(request, code):
    raise Http404

def new_lang(request):
    form = langForms.LanguageForm(request.POST or None)

    if form.is_valid():
        new_language_model = form.save(commit=False)

        # Get profile corresponding to the current user
        corresponding_profile = UserProfile.objects.filter(user=request.user)
        new_language_model.profile = corresponding_profile.get(pk=1)
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
