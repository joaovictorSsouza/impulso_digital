from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from employee.models import Employee, Sector, Hierarchical_Level
from employee.forms import EmployeeModelForm
from django.db.models import Q

def EmployeeViews(request):
    search_query = request.GET.get('q', '')
    if search_query:
        # Filtra por nome OU cpf que contenham o termo de busca (case-insensitive)
        employees = Employee.objects.filter(
            Q(name__icontains=search_query) | Q(cpf__icontains=search_query) | Q(sector__sector__icontains=search_query)
        )
    else:
        employees = Employee.objects.all()
    all_sectors = Sector.objects.all()
    all_hierarchical_levels = Hierarchical_Level.objects.all()

    return render(request, 'employee.html', {'Employee': employees, 'search_query': search_query, 'sectors':all_sectors, 'hierarchical_levels': all_hierarchical_levels})

def home(request):
    return render(request, 'home.html')

def new_Employee(request):

    if request.method == 'POST':
        form_new_employee = EmployeeModelForm(request.POST, request.FILES)
        if form_new_employee.is_valid():
            form_new_employee.save()
            return redirect('Employee')
    else:
         form_new_employee = EmployeeModelForm()
    return render(request, 'new_employee.html', {'new_employee_form':form_new_employee})

def edit_employee(request, pk):
    
    employee_edit = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form_edit_employee = EmployeeModelForm(request.POST, request.FILES, instance=employee_edit)
        if form_edit_employee.is_valid():
            form_edit_employee.save()
            return redirect('Employee')
    else:
        form_edit_employee = EmployeeModelForm(request.POST, request.FILES, instance=employee_edit)
    return render(request, 'employee.html', {'form_edit_employee': form_edit_employee})

def delete_employee(request, pk):

    employee_delete = get_object_or_404(Employee, pk=pk)
    
    employee_delete.delete()
    return redirect('Employee')




