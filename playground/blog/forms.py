from django import forms
 
from .models import Membre
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Membre
        fields = ('lieu',)