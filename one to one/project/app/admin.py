from django.contrib import admin

# Register your models here.
from .models import AadharModel, StudentModel

@admin.register(AadharModel)
class AadharAdmin(admin.ModelAdmin):
    list_display=['id','AadharNo']

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['stu_name','stu_aadhar']
