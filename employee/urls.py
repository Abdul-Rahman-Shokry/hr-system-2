from django.urls import path
from . import views as EmployeeView

app_name='employee'

urlpatterns = [
    path('',EmployeeView.EmployeesView.as_view(),name="employeesList"),
    path('employee/<int:employee_id>',EmployeeView.EmployeeDetailsView.as_view(),name="EmployeeDetails"),
    path('new-employee',EmployeeView.newEmployee,name="newEmployee"),
    path('employee/<int:employee_id>/newPosition',EmployeeView.newPositionToEmployeeView.as_view(),name="newPositionToEmployee"),
    path('employee/<int:employee_id>/editPosition/<int:position_id>',EmployeeView.editPositionToEmployeeView.as_view(),name="editPositionToEmployee"),
    path('employee/<int:employee_id>/edit', EmployeeView.editEmployeeView.as_view(), name="editEmployee"),
]