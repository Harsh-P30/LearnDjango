from django import forms
from django.views import View
from .models import info


class infoForm(forms.ModelForm): # creating a form for the info model
    class Meta:
        model = info
        fields = ['name', 'address']