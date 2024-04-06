from django import forms
from .models import Snippet

class PasteForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ["title", "content"]
