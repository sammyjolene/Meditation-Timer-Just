from django import forms
from .models import Timer


class CustomTimer(forms.ModelForm):
    class Meta:
        model = Timer 
        fields = ('meditation_length', 'interval_length')
        

