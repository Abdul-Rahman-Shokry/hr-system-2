from django.urls import path
from . import views as compView

urlpatterns = [
    path('',compView.BranchesView.as_view(),name="branches"),
    path('branche/<int:branche_id>',compView.BrancheDetailsView.as_view(),name="branchesDetails"),
    path('newbranche',compView.newBranche,name="newBranche"),
    path('branche/<int:branche_id>/newDepartment',compView.newDepartmentToBrancheView.as_view(),name="newDepartmentToBranche"),
    path('branche/<int:branche_id>/editDepartment/<int:depaertment_id>',compView.editDepartmentToBrancheView.as_view(),name="editDepartmentToBranche"),
    path('branche/<int:branche_id>/edit', compView.editBrancheView.as_view(), name='editBranche'),
]