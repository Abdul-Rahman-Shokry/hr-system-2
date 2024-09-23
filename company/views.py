from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import branches,departments
from .forms import newDepartmentToBrancheForm,editDepartmentToBrancheForm
from django.views.generic import ListView,CreateView


# Create your views here.
# def Branches(request):
#     b = branches.objects.all()
#     return render(request,'company/branches.html',{'branches':b})

class BranchesView(ListView):
    model = branches
    template_name = 'company/branches.html'
    context_object_name = 'branches'
    paginate_by = 5

# def BrancheDetails(request,branche_id):
#     b= branches.objects.get(pk=branche_id)
#     return render(request,'company/brancheDetails.html',{'branche':b})

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


# def newDepartmentToBranche(request,branche_id):
#     b = branches.objects.get(pk=branche_id)
#     form = newDepartmentToBrancheForm()
#     if request.method == 'POST':
#         form = newDepartmentToBrancheForm(request.POST)
#         if form.is_valid():
#             if departments.objects.filter(name = form.cleaned_data['name'],branch_id = branche_id).exists():
#                 form.add_error('name','this department is already exists in this branch')
#                 return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':b})

#             department = form.save(commit=False)
#             department.branch_id = branche_id
#             department.save()
#             return render(request,'company/brancheDetails.html',{'branche':b})
#     # print(form)
#     # print(form.fields)
#     return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':b})

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
        
    

# def editDepartmentToBranche(request,branche_id,depaertment_id):
#     form = editDepartmentToBrancheForm()
#     b = branches.objects.get(pk=branche_id)
#     dept = departments.objects.get(pk=depaertment_id)
#     form.fields['name'].initial = dept.name
#     form.fields['description'].initial = dept.description
#     if request.method == "POST":
#         form = editDepartmentToBrancheForm(request.POST)
#         if form.is_valid():
#             deptformData = form.save(commit=False)
#             dept.name = deptformData.name
#             dept.description = deptformData.description
#             dept.save()
#             return render(request,'company/brancheDetails.html',{'branche':b})
#     return render(request,'company/editDepartmentToBranche.html',{'form':form,'branche':b,'dept':dept})

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



    

