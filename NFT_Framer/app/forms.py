from django import forms 
from .models import Template, Frame  

class FrameForm(forms.ModelForm):
    class Meta:
        model = Frame 
        fields = ['name', 'template', 'variables', 'file']
        exclude = ['user']
