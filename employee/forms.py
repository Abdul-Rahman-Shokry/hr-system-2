from django import forms
from .models import Position 


class newPositionToEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Position
        fields = ['name','years_of_experience','description']


class editPositionToEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Position
        fields = ['name','years_of_experience','description']