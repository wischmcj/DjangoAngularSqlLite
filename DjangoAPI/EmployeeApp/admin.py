from EmployeeApp.models import Departments, Employees
from django.contrib import admin

# Register your models here.from .models import Author, Genre, Book, BookInstance

admin.site.register(Employees)
admin.site.register(Departments)