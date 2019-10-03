from django import forms
from . import models as langModels

class LanguageForm(forms.ModelForm):
    class Meta:
        model = langModels.Language
        fields = ['code', 'name']
