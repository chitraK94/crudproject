from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):

    employees = Employee.objects.all()
    return render(request, 'crudApp/employee_list.html', {'employees':employees})


def create_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:

        form = EmployeeForm()

    return render(request, 'crudApp/create_employee.html',{'form':form})


def update_employee(request, pk):

    employees = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST , instance= employees)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:

        form = EmployeeForm(instance= employees)
    
    return render(request, 'crudApp/update_employee.html', {'employee':employees, 'form':form})


def delete_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    employee.delete()
    return redirect('employee_list')









