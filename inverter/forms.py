from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import FileInstance

class InvertImageForm(forms.Form):
    #do checks if it is an image in future lol
    #file_location = forms.ImageField(help_text="Enter an image to be uploaded")
    file_location = forms.FileField()
    the_name = forms.CharField()
    class Meta:
        model = FileInstance
        fields = ['file_location', 'name',]


