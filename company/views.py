from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
# from django.http import HttpResponse
from .models import branches,departments
from .forms import EditBrancheForm, newDepartmentToBrancheForm,editDepartmentToBrancheForm
from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView

class BranchesView(ListView):
    model = branches
    template_name = 'company/branches.html'
    context_object_name = 'branches'
    paginate_by = 5


class BrancheDetailsView(ListView):
    template_name = 'company/brancheDetails.html'
    context_object_name = 'branche'

    def get_queryset(self):
        return  branches.objects.get(pk=self.kwargs['branche_id'])

def newBranche(request):
    if request.method == 'POST':
        name = request.POST['brancheName']
        address = request.POST['brancheAddress']
        phone = request.POST['branchePhone']
        email = request.POST['brancheEmail']
        branches.objects.create(
            name= name,address= address,phone= phone,email=email
        )
    return render(request,'company/newBranche.html')



class newDepartmentToBrancheView(CreateView):
    form_class = newDepartmentToBrancheForm
    template_name = 'company/newDepartmentToBranche.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['branche'] = branches.objects.get(pk=self.kwargs['branche_id'])
        return contex

    def form_valid(self, form):
        if departments.objects.filter(name = form.cleaned_data['name'],branch_id = self.kwargs['branche_id']).exists():
            form.add_error('name','this department is already exists in this branch')
            return self.form_invalid(form)

        department = form.save(commit=False)
        department.branch_id = self.kwargs['branche_id']
        department.save()
        return redirect('branchesDetails',branche_id =  self.kwargs['branche_id'])



class editDepartmentToBrancheView(CreateView):
    form_class = newDepartmentToBrancheForm
    template_name = 'company/editDepartmentToBranche.html'

    def dispatch(self, request, *args, **kwargs):
        self.dept = departments.objects.get(pk=self.kwargs['depaertment_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        dept = departments.objects.get(pk=self.kwargs['depaertment_id'])
        initial = super().get_initial()
        initial['name'] = dept.name
        initial['description'] = dept.description
        return initial

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['branche'] = branches.objects.get(pk=self.kwargs['branche_id'])
        contex['dept'] = self.dept
        return contex

    def form_valid(self, form):
        # if departments.objects.filter(name = form.cleaned_data['name'],branch_id = self.kwargs['branche_id']).exists():
        #     form.add_error('name','this department is already exists in this branch')
        #     return self.form_invalid(form)
        dept = self.dept
        deptformData = form.save(commit=False)
        dept.name = deptformData.name
        dept.description = deptformData.description
        dept.save()
        return redirect('branchesDetails',branche_id =  self.kwargs['branche_id'])


class editBrancheView(UpdateView):
    model = branches
    form_class = EditBrancheForm
    template_name = 'company/editBranche.html'
    pk_url_kwarg = 'branche_id'
    context_object_name = 'branche'

    def get_success_url(self):
        return reverse('branchesDetails', kwargs={'branche_id': self.object.pk})



