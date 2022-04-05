from django.db import models

# Create your models here.
class student(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cUID = models.CharField(max_length=100, null=False, default='')
    cpassword = models.CharField(max_length=100, null=False, default='')    
    cSex = models.CharField(max_length=2, default='M', null=False)


	
    def __str__(self):
        return self.cName
