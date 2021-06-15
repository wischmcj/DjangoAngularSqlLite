from django.shortcuts import render
from django.views.decorators.csrf import crsf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


# Create your views here.

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

def departmentApi(request,id =0):
        if request.method == GET:
            departments = Departments.objects.all()
            departments_serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data,safe=False)

        elif request.method == 'POST':
            department_data=JSONParser().parse(request)
            departments_serializer = DepartmentSerializer(data =department_data)
            if departments_serializer.isValid():
                    departments_serializer.save
                    return  JsonResponse('Data saved successfully!',safe=False)
            return  JsonResponse('Failed to add',safe=False)

        elif request.method == 'PUT':
            department_data = JSONParser().parse(request)
            department=Departments.objects.get(DepartmentId=department_data['DepartmentID'])
            department_serializer = DepartmentSerializer(department,data=department_data)
            if department_serializer.is_valid():
                department_serializer.save()
                return  JsonResponse('Data updated successfully!',safe=False)
            JsonResponse('Failed to add',safe=False)

        elif request.method == 'DELETE':
            department = Departments.objects.get(DepartmentsId= id)
            department.delete();
            return  JsonResponse('Data deleted successfully!',safe=False)