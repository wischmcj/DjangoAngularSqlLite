from django.db import models

# # Create your models here.

class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName =models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

class DepartmentConsumer(object):

    def __init__(self, name=None):
        self.name = name

    class Meta:
        managed = False


class DepartmentProducer(object):

    def __init__(self, name):
        self.name = name

    class Meta:
        managed = False