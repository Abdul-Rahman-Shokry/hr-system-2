from django import forms
from .models import departments, branches 


class newDepartmentToBrancheForm(forms.ModelForm):
    
    class Meta:
        model = departments
        fields = ['name','description']


class editDepartmentToBrancheForm(forms.ModelForm):
    
    class Meta:
        model = departments
        fields = ['name','description']


class EditBrancheForm(forms.ModelForm):
    class Meta:
        model = branches
        fields = ['name', 'address', 'phone', 'email']