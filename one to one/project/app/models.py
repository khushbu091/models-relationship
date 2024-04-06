from django.db import models

# Create your models here.
class AadharModel(models.Model):
    AadharNo=models.IntegerField()

    def __str__(self):
        return str(self.AadharNo)
    
class StudentModel(models.Model):
    stu_name=models.CharField(max_length=500)
    stu_add=models.CharField(max_length=500)
    stu_aadhar=models.OneToOneField(AadharModel,on_delete=models.CASCADE,primary_key=True)
    #stu_aadhar=models.OneToOneField(AadharModel,on_delete=models.PROTECT,primary_key=True)

    class Meta:
        def __str__(self):
            return(self.stu_name)
