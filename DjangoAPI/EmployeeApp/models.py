from django.db import models

# # Create your models here.
class Departments(models.Model):
    DeparmentID = models.AutoField(primary_key=True)
    DeparmentName =models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length =100)
    Department = models.CharField(max_length =100)
    EmpoyeeId = models.DateField()
    PhotoFileName = models.CharField(max_length =100)