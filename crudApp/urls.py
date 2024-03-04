from django.urls import path
from . import views

urlpatterns = [

    path('employee_list/', views.employee_list, name = 'employee_list'),
    path('create_employee/', views.create_employee, name = 'create_employee'),
    path('update_employee/<int:pk>/', views.update_employee, name = 'update_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name = 'delete_employee'),
    
]
