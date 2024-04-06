from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    dep_name=models.CharField(max_length=100,verbose_name='Name')
    description = models.TextField(max_length=200,verbose_name='Decs')

    def __str__(self):
        return self.dep_name
    
class StudentModel(models.Model):
    stu_name=models.CharField(max_length=500)
    stu_add=models.CharField(max_length=500)
    stu_email=models.EmailField()
    stu_mobile=models.IntegerField()
    #stu_aadhar=models.Foreignkey(Department,on_delete=models.CASCADE,primary_key=True)
    stu_department=models.ForeignKey(DepartmentModel,on_delete=models.PROTECT)

    # class Meta:
    #     def __str__(self):
    #         return(self.stu_name)
from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    dep_name=models.CharField(max_length=100,verbose_name='Name')
    description = models.TextField(max_length=200,verbose_name='Decs')

    def __str__(self):
        return self.dep_name
    
class StudentModel(models.Model):
    stu_name=models.CharField(max_length=500)
    stu_add=models.CharField(max_length=500)
    stu_email=models.EmailField()
    stu_mobile=models.IntegerField()
    #stu_aadhar=models.Foreignkey(Department,on_delete=models.CASCADE,primary_key=True)
    stu_department=models.ForeignKey(DepartmentModel,on_delete=models.PROTECT)

    # class Meta:
    #     def __str__(self):
    #         return(self.stu_name)
