
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        Employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(Employees_serializer.data, safe=False)

    elif request.method=='POST':
        Employee_data=JSONParser().parse(request)
        Employee_serializer = EmployeeSerializer(data=Employee_data)
        if Employee_serializer.is_valid():
            Employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        Employee_data = JSONParser().parse(request)
        Employee=Employees.objects.get(EmployeeID=Employee_data['EmployeeID'])
        Employee_serializer=EmployeeSerializer(Employee,data=Employee_data)
        if Employee_serializer.is_valid():
            Employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        Employee=Employees.objects.get(EmployeeID=id)
        Employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

      
@csrf_exempt
def SaveFiles(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)