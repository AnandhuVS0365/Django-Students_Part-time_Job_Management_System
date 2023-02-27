from distutils.command.upload import upload
from msilib.schema import Class
from django.db import models

# Create your models here.

class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()
    

    def __str__(self):
        return self.dept_name
class jobs(models.Model):
    job_title = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    job_category = models.ForeignKey(departments,on_delete=models.CASCADE)
    job_image =models.ImageField(upload_to= 'jobs')

class login(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Email_address = models.EmailField()
    Password = models.CharField(max_length=50)
    Logged_on =models.DateField(auto_now=True)
   

    def __str__(self):
        return self.First_name
        

        