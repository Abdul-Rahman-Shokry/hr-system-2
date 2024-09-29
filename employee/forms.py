from django import forms
from .models import Position, Employee


class newPositionToEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Position
        fields = ['name','years_of_experience','description']


class editPositionToEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Position
        fields = ['name','years_of_experience','description']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'salary'] 