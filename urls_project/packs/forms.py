from dataclasses import field, fields
from django import forms
from .models import Package

class PackageForm(forms.ModelForm):

    class Meta():
        model = Package
        fields = ('name','description')
