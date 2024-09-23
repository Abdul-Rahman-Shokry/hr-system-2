from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .models import Employee,Position
from .forms import newPositionToEmployeeForm,editPositionToEmployeeForm
from django.views.generic import ListView,CreateView



class EmployeesView(ListView):
    model = Employee
    template_name = 'employee/employees.html'
    context_object_name = 'employees'
    paginate_by = 5

class EmployeeDetailsView(ListView):
    template_name = 'employee/employeeDetails.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return  Employee.objects.get(pk=self.kwargs['employee_id'])

def newEmployee(request):
    if request.method == 'POST':
        name = request.POST['employeeName']
        age = request.POST['employeeAge']
        salary = request.POST['employeeSalary']
        Employee.objects.create(
            name= name,age= age,salary=salary,
        )
    return render(request,'employee/newEmployee.html')


class newPositionToEmployeeView(CreateView):
    form_class = newPositionToEmployeeForm
    template_name = 'employee/newPositionToEmployee.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['employee'] = Employee.objects.get(pk=self.kwargs['employee_id'])
        return contex

    def form_valid(self, form):
        if Position.objects.filter(name = form.cleaned_data['name'],employee_id = self.kwargs['employee_id']).exists():
            form.add_error('name','this position is already associated with this employee')
            return self.form_invalid(form)

        position = form.save(commit=False)
        position.employee_id = self.kwargs['employee_id']
        position.save()
        return redirect('EmployeeDetails',employee_id =  self.kwargs['employee_id'])
        
    


class editPositionToEmployeeView(CreateView):
    form_class = newPositionToEmployeeForm
    template_name = 'employee/editPositionToEmployee.html'

    def dispatch(self, request, *args, **kwargs):
        self.dept = Position.objects.get(pk=self.kwargs['position_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        pos = Position.objects.get(pk=self.kwargs['position_id'])
        initial = super().get_initial()
        initial['name'] = pos.name
        initial['description'] = pos.description
        return initial

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['employee'] = Employee.objects.get(pk=self.kwargs['employee_id'])
        contex['pos'] = self.pos
        return contex

    def form_valid(self, form):
        pos = self.pos
        posformData = form.save(commit=False)
        pos.name = posformData.name
        pos.description = posformData.description
        pos.save()
        return redirect('EmployeeDetails',employee_id =  self.kwargs['employee_id'])



    

