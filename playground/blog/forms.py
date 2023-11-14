from django import forms
 
from .models import Membres
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Membres
        fields = ('lieu',)