from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class InvertImageForm(forms.Form):
    #do checks if it is an image in future lol
    file_location = forms.ImageField(help_text="Enter an image to be uploaded")

