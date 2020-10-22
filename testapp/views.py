from django.shortcuts import render, redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.
def Retreve_View(request):
    employees = Employee.objects.filter(esal__gt=15000)
    my_dict ={'employees':employees}
    return render(request,'testapp/index.html',context=my_dict)

def Create_View(request):
    form = EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/EmpInfo')
    my_dict={'form':form}
    return render(request,'testapp/create.html',context=my_dict)


def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/EmpInfo')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/EmpInfo')
    return render(request,'testapp/update.html',{'employee':employee})