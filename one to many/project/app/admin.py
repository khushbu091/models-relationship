from django.contrib import admin
from .models import StudentModel, DepartmentModel
# Register your models here.

admin.site.register(StudentModel)
admin.site.register(DepartmentModel)
