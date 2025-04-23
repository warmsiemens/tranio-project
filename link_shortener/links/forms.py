from django import forms
from .models import Link


class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['full_link']

    full_link = forms.URLField(label="Введите полную ссылку")
