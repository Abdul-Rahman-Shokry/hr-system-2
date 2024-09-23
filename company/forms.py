from django import forms
from .models import departments 


class newDepartmentToBrancheForm(forms.ModelForm):
    
    class Meta:
        model = departments
        fields = ['name','description']


class editDepartmentToBrancheForm(forms.ModelForm):
    
    class Meta:
        model = departments
        fields = ['name','description']
