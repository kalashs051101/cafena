from django import forms
from .models import *
 
 
class uploader_file_form(forms.ModelForm):
    class Meta:
        model = upload_model
        fields = ['desc', 'file']